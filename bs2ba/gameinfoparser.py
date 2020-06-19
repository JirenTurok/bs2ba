# Copyright (c) 2020 Roman Trapeznikov

def find_and_parse(s: str):
    for infotype in ('name', 'description'):
        while f'def get_{infotype}' in s:
            lines = s.splitlines()
            lineno = 0
            for line in lines:
                if f'def get_{infotype}' in line:
                    break
                lineno += 1
            lineno -= 1 # @classmethod
            begin = lineno
            end = lineno + 1
            for line in lines[end + 1:]:
                if (line.strip().startswith('def') or 
                        line.strip().startswith('@')):
                    end = lineno + 1
                    break
                lineno += 1
            name = '\n'.join(lines[begin:end])
            name = name.split('return', 1)[1].strip()
            s = '\n'.join(lines[:begin] + [f'    {infotype} = {name}'] + lines[end:])
    return s
