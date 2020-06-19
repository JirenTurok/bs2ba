# Copyright (c) 2020 Roman Trapeznikov

import json

SETTINGS_BEGIN = '['
SETTINGS_END = ']'


def parse_setting_obj(obj: dict):
    result = f'    available_settings = {SETTINGS_BEGIN}\n'
    for key, value in obj:
        if 'choices' in value:
            default = value.get('default')
            stype = 'Int' if all(map(lambda x: isinstance(x[1], int), value['choices'])) else 'Float'
            result += ((f'        ba.{stype}ChoiceSetting(\n') +
                       (f'            "{key}",\n') +
                       (f'            choices={value["choices"]},\n') + 
                       (f'            default={default},\n' if default is not None else '') + 
                       (f'        ),\n'))
        else:
            default = value.get('default')
            increment = value.get('increment')
            max_value = value.get('max_value')
            min_value = value.get('min_value')
            if default is None and max_value is None:
                raise Exception('Incorrect settings! default not found for', key)
            stype = ('Bool' if isinstance(default, bool) else
                     'Float' if isinstance(default, float) else
                     'Int')
            result += ((f'        ba.{stype}Setting(\n') +
                       (f'            "{key}",\n') +
                       (f'            default={default},\n' if default is not None else '') +
                       (f'            min_value={min_value},\n' if min_value is not None else '') +
                       (f'            max_value={max_value},\n' if max_value is not None else '') +
                       (f'            increment={increment},\n' if increment is not None else '') +
                       (f'        ),\n'))
    result += f'    {SETTINGS_END}'
    return result



def parse_settings(s: str):
    settings = SETTINGS_BEGIN + SETTINGS_END.join(
        s.split(SETTINGS_BEGIN, 1)[1].split(SETTINGS_END)[:-1]) + SETTINGS_END
    settings = settings.replace("'", '"')
    settings = settings.replace('(', '[').replace(')', ']')
    settings = settings.replace('True', 'true')
    settings = settings.replace('False', 'false')
    try:
        obj = json.loads(settings)
    except Exception as e:
        import traceback
        print('Error while parsing settings! Please remove unneeded ",".')
        traceback.print_exception(e.__class__, e, e.__traceback__)
        exit(1)
    result = parse_setting_obj(obj)
    return result


def find_and_parse(s: str):
    while 'def get_settings' in s:
        lines = s.splitlines()
        lineno = 0
        for line in lines:
            if 'def get_settings' in line:
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
        settings = parse_settings('\n'.join(lines[begin:end]))
        s = '\n'.join(lines[:begin] + [settings] + lines[end:])
    return s
