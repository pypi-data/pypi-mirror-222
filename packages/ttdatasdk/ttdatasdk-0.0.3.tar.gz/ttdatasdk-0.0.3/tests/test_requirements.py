import os
import sys
import re
from setuptools import setup, find_packages

THIS_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _parse_requirement_file(path):
    if not os.path.isfile(path):
        return []
    with open(path) as f:
        requirements = [line.strip() for line in f if line.strip()]
    return requirements


def get_install_requires():
    requirement_file = os.path.join(THIS_FOLDER, "requirements.txt")
    return _parse_requirement_file(requirement_file)


ret = get_install_requires()
print(ret)
