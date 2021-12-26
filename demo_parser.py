from csgo.parser import DemoParser
from os import walk


def parse_demo(demo_file_path: str, demo_name: str):
    try:
        demo_parser = DemoParser(demofile='../../../Volumes/LaraHDD/demos/' + demo_file_path, demo_id='./parsed_demos/' + demo_name, parse_rate=128)
        demo_parser.parse()
    except Exception as e:
        print(e)

demo_file_paths = next(walk('../../../Volumes/LaraHDD/demos'), (None, None, []))[2]
json_file_paths = next(walk('./parsed_demos'), (None, None, []))[2]
json_file_names = [x.split('.')[0] for x in json_file_paths if x.endswith('.json')]

for file_path in demo_file_paths:
    if file_path.split('.')[0] not in json_file_names:
        parse_demo(file_path, file_path.split('.')[0])
    else:
        print(file_path + ' already parsed')
