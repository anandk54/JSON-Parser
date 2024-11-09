import sys
from jsonParser import json_parser, JsonException

file = open("test_input.txt")

with file as f:
    s = f.read()
    print(s)
    try:
        result = json_parser(s)
    except JsonException:
        print('The program failed with an error: ')
        sys.exit(1)
    
    print(result)