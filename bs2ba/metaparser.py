def find_and_parse(s: str):
    while f'def bs_get_api_version' in s:
        lines = s.splitlines()
        lineno = 0
        for line in lines:
            if f'def bs_get_api_version' in line:
                break
            lineno += 1
        lineno -= 1 # @classmethod
        begin = lineno
        end = lineno + 1
        for line in lines[end + 1:]:
            if (line.strip().startswith('def') or 
                    line.strip().startswith('@') or
                    line.strip().startswith('class')):
                end = lineno + 1
                break
            lineno += 1
        s = '\n'.join(lines[:begin] + [f'# ba_meta require api 6'] + lines[end:])
    
    if f'def bs_get_games' in s:
        lines = s.splitlines()
        lineno = 0
        for line in lines:
            if f'def bs_get_games' in line:
                break
            lineno += 1
        lineno -= 1 # @classmethod
        begin = lineno
        end = lineno + 1
        for line in lines[end + 1:]:
            if (line.strip().startswith('def') or 
                    line.strip().startswith('@') or
                    line.strip().startswith('class')):
                end = lineno + 1
                break
            lineno += 1
        games = '\n'.join(lines[begin:end])
        games = games.split('return', 1)[1].replace(' ', '').replace('[', '').replace(']', '')
        games = games.replace('(', '').replace(')', '').strip().split(',')
        s = '\n'.join(lines[:begin] + lines[end:])

        lineno = 0
        for game in games:
            lines = s.splitlines()
            for line in lines:
                if f'class {game}' in line:
                    break
                lineno += 1
            s = '\n'.join(lines[:lineno] + ['# ba_meta export game'] + lines[lineno:])
    return s
