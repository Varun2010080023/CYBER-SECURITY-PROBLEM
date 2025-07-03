from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    requirement_list = []
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print(f"Warning not found. No requirements will be installed.")

    return requirement_list

print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="varun",
    author_email="varun.ch1405@gmail.com@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)