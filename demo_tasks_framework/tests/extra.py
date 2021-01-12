"""Loading test data from json file"""

import os
import json


def from_file(directory, file):

    file_path = os.path.join(directory, file)
    result = []

    with open(file_path) as f:
        result = json.loads(f.read())

    return result
