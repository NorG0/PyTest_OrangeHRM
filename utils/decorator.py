from selenium.common import TimeoutException, NoSuchElementException
import functools
import logging

logger = logging.getLogger(__name__)


def log_step(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        logger.info(f"Starting: {func.__name__}")
        result = func(*args,**kwargs)
        logger.info(f"Ending: {func.__name__}")
        return result
    return wrapper


def handle_exception(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except TimeoutException:
            logger.error(f"Timeout occurred while executing {func.__name__}")
            raise
        except NoSuchElementException as e:
            logger.error(f"Element not found while executing {func.__name__}: {e}")
            raise
        except Exception as e:
            logger.error(f"Error occurred while executing {func.__name__}: {e}")
            raise
    return wrapper