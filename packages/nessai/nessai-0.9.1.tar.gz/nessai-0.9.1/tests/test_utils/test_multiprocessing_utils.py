# -*- coding: utf-8 -*-
"""
Tests for rescaling functions
"""
import multiprocessing
from multiprocessing.dummy import Pool
import pytest
import sys
from unittest.mock import MagicMock, patch

from nessai.utils.multiprocessing import (
    check_multiprocessing_start_method,
    initialise_pool_variables,
    get_n_pool,
    log_likelihood_wrapper,
)


def test_pool_variables():
    """Assert initialising the variables and calling the likelihood work"""
    model = MagicMock()
    model.log_likelihood = lambda x: x
    initialise_pool_variables(model)
    pool = Pool(1)
    out = pool.map(log_likelihood_wrapper, [1, 2, 3])
    pool.close()
    pool.terminate()
    assert out == [1, 2, 3]

    # Reset to the default value
    initialise_pool_variables(None)


@pytest.mark.parametrize("method", ["fork", "forkserver", "spawn"])
def test_check_multiprocessing_start_method(method, caplog):
    """
    Test check multiprocessing start method passes for all methods
    """
    with patch("multiprocessing.get_start_method", return_value=method):
        check_multiprocessing_start_method()
    if method != "fork":
        assert "This may lead to high memory usage or errors" in caplog.text


@pytest.mark.integration_test
@pytest.mark.skip_on_windows
def test_check_multiprocessing_start_method_integration():
    """Integration test for checking the start method."""
    mp = multiprocessing.get_context("fork")
    with patch("multiprocessing.get_start_method", mp.get_start_method):
        check_multiprocessing_start_method()


@pytest.mark.parametrize("method", ["fork", "forkserver", "spawn"])
@pytest.mark.integration_test
def test_check_multiprocessing_start_method_error_integration(method, caplog):
    """Integration test for checking the start method prints a warning"""
    if sys.platform == "win32" and method != "spawn":
        pytest.skip("Windows only supports the 'spawn' start method")
    mp = multiprocessing.get_context(method)
    with patch("multiprocessing.get_start_method", mp.get_start_method):
        check_multiprocessing_start_method()
    if method != "fork":
        assert "This may lead to high memory usage or errors" in caplog.text


def test_model_error():
    """Assert an error is raised in the global variables have not been \
        initialised
    """
    model = MagicMock()
    model.log_likelihood = lambda x: x
    pool = Pool(1)
    with pytest.raises(AttributeError) as excinfo:
        pool.map(log_likelihood_wrapper, [1, 2, 3])
    assert "'NoneType' object has no attribute 'log_likelihood'" in str(
        excinfo.value
    )
    pool.close()
    pool.terminate()


def test_get_n_pool_processes():
    """ "Assert the correct value is returned if the pool has a `_processes`
    attribute.
    """
    pool = MagicMock(spec=Pool)
    pool._processes = 4
    assert get_n_pool(pool) == 4


def test_get_n_pool_ray():
    """ "Assert the correct value is returned if the pool has a `_actor_pool`
    attribute (e.g. ray.util.multiprocessing.Pool).
    """
    pool = MagicMock()
    del pool._processes
    pool._actor_pool = 4 * [0]
    assert get_n_pool(pool) == 4


def test_get_n_pool_unknown():
    """ "Assert None is returned if the type of pool is not known."""
    pool = MagicMock()
    del pool._processes
    del pool._actor_pool
    assert get_n_pool(pool) is None
