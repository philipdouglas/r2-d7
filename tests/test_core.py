import pytest

from r2d7.core import BotCore


# @pytest.mark.parametrize('name, stripped', [
#     ('Kath Scarlett', 'Kath Scarlett'),
#     ('"Dutch" Vander', '"Dutch" Vander')
# ]
# def test_

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

    assert data['ships']['xwing']['name'] == 'X-Wing'
    assert data['conditions']['adebttopay']['id'] == 3
