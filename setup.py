from setuptools import setup, find_packages
import re, os

on_rtd = os.getenv('READTHEDOCS') == 'True'

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

readme = ''
with open('README.md') as f:
    readme = f.read()

setup(name='pya3rt',
      author='nocotan',
      url='https://github.com/nocotan/pya3rt',
      version=1.1,
      packages=find_packages(),
      license='MIT',
      description='A python wrapper for A3RT API',
      long_description=readme,
      include_package_data=True,
      install_requires=requirements,
)
