## SETTING UP A PACKAGE OF THE ML APPLICATION 

from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads the requirements file and returns a list of required packages.
    It excludes the '-e .' entry if present.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('-e')]
    
    return requirements

# Setup configuration for the package
setup(
    name='ML_Project',
    version='0.0.1',
    author='Kripesh Das',
    author_email='kripeshdas2jio@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)