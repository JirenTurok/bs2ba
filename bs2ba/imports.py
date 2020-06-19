def optimize_imports(s):
    return s



def _genimports(module, names):
    result = ''
    for name in names:
        result += f'from {module} import {name}\n'
    return result

def genimports(imps):
    result = ''
    for imp in imps:
        result += _genimports(*imp)
    return result



imports = genimports((
    ('bastd.actor.spaz', ('Spaz',)),
    ('bastd.actor.scoreboard', ('Scoreboard',)),
    ('bastd.actor.playerspaz', ('PlayerSpaz',)),
    ('bastd.actor.powerupbox', ('PowerupBox')),
    ('bastd.gameutils', ('SharedObjects',))
))
