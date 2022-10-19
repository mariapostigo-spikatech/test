from pathlib import Path
from setuptools import find_namespace_packages, setup

NAME = 'test_project'
DESCRIPTION = 'My short description for my project.'
URL = ''
EMAIL = 'nombre.apellido@spikatech.com'
AUTHOR = 'Nombre apellido'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.0'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    packages=find_namespace_packages(),
    )
