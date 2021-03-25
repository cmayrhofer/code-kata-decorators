import logging
import time
from typing import List

import pytest

from exercises.exercises import catch_exception, log_execution_time

logging.basicConfig(level=logging.INFO)


@log_execution_time
def fancy_function(number: int, duration: int = 5) -> List:
    """A not so fancy function."""
    time.sleep(duration)
    return list(range(number))


ERROR_MSG_1 = "That was the wrong number"
ERROR_MSG_2 = "Actually it's not an AssertionError"
ERROR_MSG_3 = "Only klaus is yet implemented"


@catch_exception
def faulty_function(number: int, name: str = "Klaus") -> List:
    """A rather faulty function"""
    if number == 1:
        raise ValueError(ERROR_MSG_1)
    elif number == 2:
        raise AssertionError(ERROR_MSG_2)
    elif name != "Klaus":
        raise NotImplementedError(ERROR_MSG_3)
    return list(range(number))


def test_log_execution_time(caplog):
    caplog.set_level(logging.INFO)
    DURATION = 1
    NUMBER = 4
    result = fancy_function(NUMBER, duration=DURATION)
    LOG_MSG = f"The function: fancy_function took {DURATION}s to execute."
    # check that return value is as expected
    assert result == list(range(NUMBER))
    # Check log message
    record = caplog.record_tuples[-1]
    assert record[0] == "exercises.exercises"
    assert record[1] == logging.INFO
    assert record[2] == LOG_MSG


def test_catch_exception(caplog):
    caplog.set_level(logging.CRITICAL)
    # check ordinary behaviour
    NUMBER, NAME = 42, "Klaus"
    result = faulty_function(NUMBER, name=NAME)
    assert result == list(range(NUMBER))
    # check exception handeling
    for error, num, name, error_msg in (
        (ValueError, 1, "klaus", ERROR_MSG_1),
        (AssertionError, 2, "klaus", ERROR_MSG_2),
        (NotImplementedError, 42, "Gustav", ERROR_MSG_3),
    ):
        with pytest.raises(error):
            faulty_function(num, name=name)
            record = caplog.record_tuples[-1]
            assert record[0] == "exercises.exercises"
            assert record[1] == logging.CRITICAL
            assert record[2] == error_msg
