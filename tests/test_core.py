import threading

import pytest

from r2d7.core import DroidCore


categories = [
    'condition',
    'damage',
    'pilot',
    'ship',
    'upgrade',
]

def test_data(testbot):
    for filename in categories:
        assert filename in testbot.data

    assert testbot.data_version is not None
    assert testbot.data['ship']['starviperclassattackplatform']['name'] == "StarViper-class Attack Platform"
    assert testbot.data['upgrade']['genius']['name'] == "\"Genius\""
    assert type(testbot.data['ship']['hwk290lightfreighter']['pilots']) is dict


partial_canonicalize_tests = {
    'X-Wing': 'xwing',
    'T-70 X-Wing': 't70xwing',
    'Veteran instincts': 'veteraninstincts',
}
@pytest.mark.parametrize('before, after', partial_canonicalize_tests.items())
def test_partial_canonicalize(before, after):
    assert DroidCore.partial_canonicalize(before) == after


def test_needs_update(testbot):
    assert testbot.data_version is not None
    assert not testbot.needs_update()


def test_threaded(testbot):
    def threadtest(signal):
        # If a new event loop isn't created for the thread, this will crash
        try:
            assert threading.current_thread() != threading.main_thread()
            testbot.load_data()
        except Exception as error:
            # Pytest will catch this stdout and print it and the signal will
            # fail the test
            print(error)
            signal.clear()
        else:
            signal.set()

    signal = threading.Event()
    thread = threading.Thread(target=threadtest, args=(signal, ))
    thread.start()
    thread.join()
    assert signal.is_set()

