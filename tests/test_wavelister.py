import pytest

from r2d7.wavelister import WaveLister
from r2d7.slackdroid import SlackDroid

@pytest.fixture(scope="module")
def testbot():
    class TestBot(SlackDroid, WaveLister):
        pass
    bot = TestBot()
    bot.load_data()
    return bot

print_wave_tests = (
    ('0', [
        '*Wave 0* - September 2012, September 2015',
        '- <http://xwing-miniatures.wikia.com/wiki/X-Wing_Core_Set|Core Set> (X-Wing, TIE Fighter x2)',
        '- <http://xwing-miniatures.wikia.com/wiki/X-Wing_The_Force_Awakens_Core_Set|The Force Awakens Core Set> (T-70 X-Wing, TIE/fo Fighter x2)',
    ]),
    ('1', [
        '*Wave 1* - September 2012',
        '- <http://xwing-miniatures.wikia.com/wiki/X-Wing_Expansion_Pack|X-Wing Expansion Pack>',
        '- <http://xwing-miniatures.wikia.com/wiki/Y-Wing_Expansion_Pack|Y-Wing Expansion Pack>',
        '- <http://xwing-miniatures.wikia.com/wiki/TIE_Fighter_Expansion_Pack|TIE Fighter Expansion Pack>',
        '- <http://xwing-miniatures.wikia.com/wiki/TIE_Advanced_Expansion_Pack|TIE Advanced Expansion Pack>',
    ]),
    ('7', [
        '*Wave 7* - August 2015',
        '- <http://xwing-miniatures.wikia.com/wiki/Hound\'s_Tooth_Expansion_Pack|Hound\'s Tooth Expansion Pack> (YV-666)',
        '- <http://xwing-miniatures.wikia.com/wiki/Kihraxz_Fighter_Expansion_Pack|Kihraxz Fighter Expansion Pack>',
        '- <http://xwing-miniatures.wikia.com/wiki/K-Wing_Expansion_Pack|K-Wing Expansion Pack>',
        '- <http://xwing-miniatures.wikia.com/wiki/TIE_Punisher_Expansion_Pack|TIE Punisher Expansion Pack>',
    ])
)
@pytest.mark.parametrize('wave, output', print_wave_tests)
def test_print_wave(testbot, wave, output):
    assert testbot.print_wave(wave) == output
