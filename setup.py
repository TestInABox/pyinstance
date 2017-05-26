import sys
from setuptools import setup, find_packages

REQUIRES = []

setup(
    name='pyinstance',
    version='1.0',
    description='Python Object Instance Management',
    license='Apache License 2.0',
    url='https://github.com/TestInABox/pyinstance',
    author='Benjamen R. Meyer',
    author_email='bm_witness@yahoo.com',
    install_requires=REQUIRES,
    test_suite='pyinstance',
    packages=find_packages(exclude=['tests*', 'pyinstance/tests']),
    zip_safe=True,
    classifiers=["Intended Audience :: Developers",
                 "License :: OSI Approved :: MIT License",
                 "Topic :: Software Development :: Testing"],
)
