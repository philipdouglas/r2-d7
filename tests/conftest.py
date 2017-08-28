import pytest
from r2d7.slack.__main__ import Droid


@pytest.fixture(scope="session")
def testbot():
    bot = Droid()
    bot.load_data()
    return bot
