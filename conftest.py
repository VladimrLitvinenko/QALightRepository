import logging
import random


def pytest_runtest_setup(item):
    """prepare test"""
    log = logging.getLogger(item.name)
    item.cls.logger = log
    item.cls.variety = str(random.randint(10000000, 99999999))


class BaseTest:
    """BaseTest class for inheritance.Implements test class default variables"""
    logger = logging.getLogger(__name__)
    variety = str(random.randint(10000000, 99999999))
