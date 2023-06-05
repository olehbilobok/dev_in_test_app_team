import pytest
from framework.sidebar import Sidebar


@pytest.fixture(scope='function')
def sidebar_fixture(driver):
    yield Sidebar(driver)
