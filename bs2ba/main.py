import re
from bs2ba import settingsparser, gameinfoparser, metaparser
from bs2ba.subs import patterns
from bs2ba.imports import imports, optimize_imports
import argparse

def main(args=None) -> None:
    parser = argparse.ArgumentParser(
        usage='bs2ba [options] file',
        prog='bs2ba',
        description='Easy way to convert mods from 1.4 to 1.5 BombSquad API',
        epilog='YOU MUST KNOW FOLLOWING:\n'
               '  - bs2ba does not convert milliseconds to seconds\n'
               '  - create Player and Team classes for games;\n'
               '      pass these classes to .getplayer() methods\n'
               '  - check on_transition_in: music argument replaced\n'
               '      with default_music attribute of game class\n'
               '  - Check ba.Timer instances; for one-shot timers use ba.timer()',
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file', help='input file')
    ns = parser.parse_args(args)

    result = ''
    with open(ns.file) as f:
        result = f.read()
    for pattern in patterns:
        result = re.sub(pattern[0], pattern[1], result)
    result = settingsparser.find_and_parse(result)
    result = gameinfoparser.find_and_parse(result)
    result = metaparser.find_and_parse(result)
    result = imports + '\n' + result
    result = optimize_imports(result)
    print(result)
