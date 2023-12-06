#!/usr/bin/python3
'''load from json'''

import json


def load_from_json_file(filename):
    '''load from json'''

    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
        return data
