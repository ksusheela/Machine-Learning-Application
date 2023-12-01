from setuptools import find_packages,setup
from typing import List

REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()-> List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        requirement_list =requirements_file.readlines()
    requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]

    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)

    return requirement_list

setup(name="cost_prediction",
      version = "0.0.1",
      description = "Data science projects",
      author = "Susheela kothakonda",
      author_email = "sushe9sushe@gmail.com",
      packages = find_packages(),
      install_requires =  get_requirements(),
      
      )