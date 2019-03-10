import os
from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='supersonic',
    version='1.0',
    packages=find_packages(),
    description=('Lightning fast super customizable progress bar & indicator library for Python'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Bill Kudo',
    author_email='bluesky42624@gmail.com',
    license='GNU AGPLv3',
    url='',
    keywords='progress bar indicator supersonic',
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python",
        "Topic :: System :: Logging",
    ],
)
