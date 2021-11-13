from collections import OrderedDict
from json import JSONDecoder

last_counter = dict()

"""
parse_object_pairs is to handle duplicate keys in json by adding the number of times a key has appeared using 
last_counter. 
"""


def make_unique(key, dct):
    unique_key = key
    if unique_key in last_counter:
        last_counter[unique_key] += 1
    else:
        last_counter[unique_key] = 1
    counter = last_counter[unique_key]
    unique_key = '{}_{}'.format(unique_key, counter)
    return unique_key


def parse_object_pairs(pairs):
    dct = OrderedDict()
    for key, value in pairs:
        if key in dct:
            key = make_unique(key, dct)
        dct[key] = value
    return dct


"""
formatName: just a formatter to exclude numbers after a drink if there are multiple requests of the same drink
"""


def formatName(name: str):
    words = name.split('_')
    if words[-1].isdigit():
        name = "_".join(words[:-1])
    return name


"""
load the json file and return the content
"""


def loadFile(file):
    with open(file, "r") as file:
        decoder = JSONDecoder(object_pairs_hook=parse_object_pairs)
        data = decoder.decode(file.read())
    return data
