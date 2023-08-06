# setup.py

from setuptools import setup, find_packages

setup(
    name='black_scholes_pyvollib_gamma',
    version='0.1.0',
    description='Custom package with only the gamma function from py_vollib',
    packages=find_packages(),
    install_requires=[
        'py_vollib[black_scholes]'
    ],
)
