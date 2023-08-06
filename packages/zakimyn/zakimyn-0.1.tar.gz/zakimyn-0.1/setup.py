# Pip_Package_Practice/setup.py
from setuptools import setup, find_packages

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setup(
    name='zakimyn', 
    version='0.1',
    description='test package',
    author='intong',
    author_email='intong@kakao.re.kr',
    long_description='description of this pypi',
    python_requires='>=3.6',
    long_description_content_type="text/markdown",
    packages= find_packages(exclude = ['docs', 'tests*','__pycache__/']),
    )