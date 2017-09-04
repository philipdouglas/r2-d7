import pytest

from r2d7.wavelister import WaveLister
from r2d7.slackdroid import SlackDroid

print_wave_tests = (
    ('0', [
        '*Wave 0*',
        '- <http://xwing-miniatures.wikia.com/wiki/X-Wing_Core_Set|Core Set> (X-wing, TIE Fighter x2) - September 2012',
        '- <http://xwing-miniatures.wikia.com/wiki/X-Wing_The_Force_Awakens_Core_Set|The Force Awakens Core Set> (T-70 X-wing, TIE/fo Fighter x2) - September 2015',
    ]),
    ('1', [
        '*Wave 1* - September 2012',
        '- <http://xwing-miniatures.wikia.com/wiki/X-Wing_Expansion_Pack|X-wing Expansion Pack>',
        '- <http://xwing-miniatures.wikia.com/wiki/Y-Wing_Expansion_Pack|Y-wing Expansion Pack>',
        '- <http://xwing-miniatures.wikia.com/wiki/TIE_Fighter_Expansion_Pack|TIE Fighter Expansion Pack>',
        '- <http://xwing-miniatures.wikia.com/wiki/TIE_Advanced_Expansion_Pack|TIE Advanced Expansion Pack>',
    ]),
    ('7', [
        '*Wave 7* - August 2015',
        '- <http://xwing-miniatures.wikia.com/wiki/Hound\'s_Tooth_Expansion_Pack|Hound\'s Tooth Expansion Pack> (YV-666)',
        '- <http://xwing-miniatures.wikia.com/wiki/Kihraxz_Fighter_Expansion_Pack|Kihraxz Fighter Expansion Pack>',
        '- <http://xwing-miniatures.wikia.com/wiki/K-Wing_Expansion_Pack|K-wing Expansion Pack>',
        '- <http://xwing-miniatures.wikia.com/wiki/TIE_Punisher_Expansion_Pack|TIE Punisher Expansion Pack>',
    ]),
    ('10', [
        '*Wave 10*',
        'December 2016',
        '- <http://xwing-miniatures.wikia.com/wiki/U-Wing_Expansion_Pack|U-wing Expansion Pack>',
        '- <http://xwing-miniatures.wikia.com/wiki/TIE_Striker_Expansion_Pack|TIE Striker Expansion Pack>',
        'February 2017',
        '- <http://xwing-miniatures.wikia.com/wiki/Sabine\'s_TIE_Fighter_Expansion_Pack|Sabine\'s TIE Fighter Expansion Pack>',
        '- <http://xwing-miniatures.wikia.com/wiki/Upsilon-class_Shuttle_Expansion_Pack|Upsilon-class Shuttle Expansion Pack>',
        '- <http://xwing-miniatures.wikia.com/wiki/Quadjumper_Expansion_Pack|Quadjumper Expansion Pack>',
    ]),
)
@pytest.mark.parametrize('wave, output', print_wave_tests)
def test_print_wave(testbot, wave, output):
    assert testbot.print_wave(wave) == output
