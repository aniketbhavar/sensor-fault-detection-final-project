from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:   #this function will Returns a list of requirements
    """
    this function will Returns a list of requirements
    """
    requirements_list:List[str] = []
    return requirements_list

setup(
    name="sensor",
    version="0.0.1",
    author="aniket",
    author_email="aniketbhavar0601@gmail.com",
    pakages=find_packages(),
    install_requires= get_requirements(),#["pymongo==4.2.0"],
)