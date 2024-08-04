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
        # Strip whitespace and filter out empty lines and '-e' entries
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('-e')]
    
    return requirements

# Setup configuration for the package
setup(
    name='ML_Project',  # Name of the project
    version='0.0.1',    # Version of the project
    author='Kripesh Das',  # Author's name
    author_email='kripeshdas2jio@gmail.com',  # Author's email
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=get_requirements('requirements.txt')  # List of dependencies
)