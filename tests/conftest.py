import pytest
from r2d7.slack.__main__ import Droid


class TestDroid(Droid):
    def test_lookup(self, descriptor):
        if '.' in descriptor:
            descriptor, num = descriptor.split('.')
        else:
            num = 0
        assert descriptor in self._lookup_data
        assert len(self._lookup_data[descriptor]) > int(num)
        return self._lookup_data[descriptor][int(num)]


@pytest.fixture(scope="session")
def testbot():
    return TestDroid()
