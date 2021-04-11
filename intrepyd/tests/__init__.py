import os

fixtures_path = os.path.dirname(__file__)

def from_fixture_path(path):
    return os.path.join(fixtures_path, path)
