import pytest

from r2d7.core import BotCore


data_files = [
    'conditions',
    # 'damage-deck-core',
    # 'damage-deck-core-tfa',
    'pilots',
    # 'reference-cards',
    'ships',
    # 'sources',
    'upgrades',
]

def test_data():
    bot = BotCore()
    data = bot.data
    for filename in data_files:
        assert filename in data

    assert data['ships']['xwing'][0]['name'] == 'X-Wing'
    assert data['conditions']['adebttopay'][0]['id'] == 3



partial_canonicalize_tests = {
    'X-Wing': 'xwing',
    'T-70 X-Wing': 't70xwing',
    'Veteran instincts': 'veteraninstincts',
}
@pytest.mark.parametrize('before, after', partial_canonicalize_tests.items())
def test_partial_canonicalize(before, after):
    assert BotCore.partial_canonicalize(before) == after
