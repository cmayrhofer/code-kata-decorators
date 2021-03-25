import logging
import time
from functools import wraps
from typing import Callable

logger = logging.getLogger(__name__)

########################################### noqa: E266, E800
############### Exercise 1 ################ noqa: E266, E800
###########################################


def log_execution_time(func: Callable) -> Callable:
    """Log the execution time of a function to INFO.

    TODO: Implement a decorator which adds the following logging statement
    after func was called in the wrapper:
        logger.info(
            f"The function: {func.__name__} took "
            f"{(end_time - start_time):.0f}s to execute."
        )
    """
    pass


###########################################
############### Exercise 2 ################ noqa: E266, E800
###########################################


def catch_exception(func: Callable) -> Callable:
    """Catch exception of function and log it to CRITICAL before raising it again.

    TODO: Implement a decorator which catches the exception raised by a
    function and logs it as follows before raising it again:
        logger.critical(
            f"The function: {func.__name__} raised the following exception:",
            exc_info=True
        )
    """
    pass
