import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import intrepyd

fixtures_path = os.path.dirname(__file__)

def from_fixture_path(path):
    return os.path.join(fixtures_path, path)
