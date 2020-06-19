import re

_underscorer1 = re.compile(r'(.)([A-Z][a-z]+)')
_underscorer2 = re.compile('([a-z0-9])([A-Z])')


def _to_snake_case(match: re.Match):
    subbed = _underscorer1.sub(r'\1_\2', match.group(0))
    res = _underscorer2.sub(r'\1_\2', subbed).lower()
    return res


def _collision_info(match: re.Match):
    s = match.group(0)
    coltype = s.split('(', 1)[1][1:].split(')', 1)[0][:-1]
    return f'ba.getcollision().{coltype}'


def _gamedata(match: re.Match):
    s = match.group(0)
    datatype = s.split('[', 1)[1][1:].split(']', 1)[0][:-1]
    return f'.{datatype}'

def _sharedobj(match: re.Match):
    s = match.group(0)
    obj = s.split('[', 1)[1][1:].split(']', 1)[0][:-1]
    return f'SharedObjects.get().{obj}'

patterns = (
    # General functions
    (r'bs\.emitBGDynamics',
        'ba.emitfx'),
    (r'bs\.shakeCamera',
        'ba.camerashake'),
    (r'bs\.getSharedObject\([\'"]globals[\'"]\)',
        'ba.getactivity().globalsnode'),
    (r'bs\.getSharedObject\(.*\)',
        _sharedobj),
    (r'bs\.getCollisionInfo\(.*\)',
        _collision_info),
    (r'bs\.getMapsSupportingPlayType',
        'ba.getmaps'),
    (r'bs\.gameTimer',
        'ba.Timer'),
    (r'bs\.getGameTime',
        'ba.time'),
    (r'bs\.getTimeString',
        'ba.timestring'),
    (r'bs\.getLanguage()',
        'ba.app.language'),
    (r'bs\.playSound',
        'ba.playsound'),
    (r'bs\.getSound',
        'ba.getsound'),
    (r'((bs)|(bsVector))\.Vector',
        'ba.Vec3'),
    (r'bs\.newNode',
        'ba.newnode'),
    (r'bs\.getActivity',
        'ba.getactivity'),
    (r'bs\.getTexture',
        'ba.gettexture'),
    (r'bs\.TeamsSession',
        'ba.MultiTeamSession'),
    (r'bs\.getModel',
        'ba.getmodel'),
    (r'bs\.ScoreBoard',
        'Scoreboard'),
    (r'bs\.Powerup',
        'PowerupBox'),
    (r'bs\.Flag',
        'Flag'),
    (r'bs\.PlayerSpazDeathMessage',
        'ba.PlayerDiedMessage'),
    (r'bs\.TeamGameResults',
        'ba.GameResults'),

    (r'bs\.',
        'ba.'),
    (r'bsInternal\.chatMessage',
        '_ba.chatmessage'),
    (r'bsInternal',
        '_ba'),
    
    # Imports
    (r'import (bs[A-Za-z]+)\n',
        ''),
    (r'import bs',
        'import ba'),
    (r'bsSpaz',
        'stdspaz'),
    (r'bsBomb',
        'stdbomb'),
    
    # Node methods
    (r'\.connectAttr', '.connectattr'),

    # Other
    (r'handleMessage',
        'handlemessage'),
    (r'\.exists\(\)',
        ''),
    (r'self\.settings',
        'self.settings_raw'),
    (r'powerup_type',
        'poweruptype'),
    (r'.auto_retain',
        'autoretain'),
    (r'.game_data',
        _gamedata),
    (r'.get_team\(\)',
        '.team'),
    (r'.get_session\(\)',
        '.session'),
    
    # Pattern for local variables, method names, etc. created by modders
    (r'[ ^_\(\)\{\}\[\]\'\"\@\!\$\%\^\*\:\,\.\<\>+-=/\\][a-z][a-zA-Z0-9]+',
        _to_snake_case)

    # ('.getInputDevice()', '.sessionplayer.inputdevice'),
    # ('getClientID()', 'client_id'),

    # ('getName', 'get_name'), # ?
    # ('getDescription', 'get_description'), # ?
    # ('getInstanceDescription', 'get_instance_description'), # ?
    # ('getInstanceScoreBoardDescription', 'get_instance_score_board_description'), # ?
    # ('getSettings', 'get_settings'), # ?
    # ('getSupportedMaps', 'get_supported_maps'), # ?
    # ('onBegin', 'on_begin'),
    # ('onTransitionIn', 'on_transition_in'),
    # ('onTeamJoin', 'on_team_join'),
    # ('endGame', 'end_game'),
    # ('supportsSessionType', 'supports_session_type'),
    # ('sessionType', 'sessiontype'),
    # ('minValue', 'min_value'),
    # ('self._isSlowMotion', 'self.slow_motion'),  # Should we use only with self?
    # ('setupStandardPowerupDrops', 'setup_standard_powerup_drops'),
    # ('setupStandardTimeLimit', 'setup_standard_time_limit'),
    # ('gameData', 'gamedata'),
    # ('getID', 'get_id'),  # Hmm
    # ('addActions', 'add_actions'),
    # ('playerMaterial', 'player_material'),
    # ('theyHaveMaterial', 'they_have_material'),
    # ('modifyPartCollision', 'modify_part_collision'),
    # ('atConnect', 'at_connect'),
    # ('projectFlagStand', 'project_flag_stand'),
    # ('getFlagPosition', 'get_flag_position'),
    # ('heightAttenuated', 'height_attenuated'),
    # ('volumeIntensityScale', 'volume_intensity_scale'),
    # ('getPlayer', 'playerspaz'),  # For message
    # ('respawnPlayer', 'respawn_player'),
    # ('opposingNode', 'opposing_node'),
    # ('getDelegate', 'getdelegate'),
    # ('getPlayer()', 'player.sessionplayer'), # :( sessionplayers... :)
    # ('.exists()', ''),  # make just sth like "if node:"
    # ('getTeam()', 'team'),
    # ('scoreSet', 'stats'),
    # ('playerScored', 'playerScored'),
    # ('bigMessage', 'big_message'),
    # ('isAlive', 'is_alive'),
    # ('getMap()', 'map'),
    # ('getStartPosition', 'get_start_position'),
    # ('setTeamScore', 'set_team_score'),
    # ('setTeamValue', 'set_team_value'),
    # ('teamFlag', 'team_flag'),
    # ('self.settings', 'self.settings_raw'),
)
