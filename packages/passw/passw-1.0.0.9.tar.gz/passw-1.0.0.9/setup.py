# setup.py
from setuptools import setup, find_packages

def get_version():
    with open("VERSION.txt") as f:
        return f.read().strip()

setup(
    name='passw',
    version=get_version(),
    packages=find_packages(),
    author='kanchan',
   
    description='A simple random password generator',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

