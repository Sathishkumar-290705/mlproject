from setuptools import find_packages,setup 
from typing import List

hypen_="-e ."

def get_requirements(file_path):
    
    """the function will return the list of requirments"""
    requierments=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ")for req in requirements]
        
        if hypen_ in requierments:
            requierments.remove(hypen_)
setup(
    name="MACHINE LEARNING",
    version="0.0.1",
    author="Sathishkumar-290705",
    author_email="sathishkumar290705@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)