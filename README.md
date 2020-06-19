# bs2ba
Easy way to convert BombSquad mods from 1.4 to 1.5 API


```
$ python -m bs2ba --help
usage: bs2ba [options] file

Easy way to convert mods from 1.4 to 1.5 BombSquad API

positional arguments:
  file        input file

optional arguments:
  -h, --help  show this help message and exit

YOU MUST KNOW FOLLOWING:
  - bs2ba does not convert milliseconds to seconds
  - create Player and Team classes for games;
      pass these classes to .getplayer() methods
  - check on_transition_in: music argument replaced
      with default_music attribute of game class
  - Check ba.Timer instances; for one-shot timers use ba.timer()
