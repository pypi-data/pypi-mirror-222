from io import open
from setuptools import setup

"""
:authors: chaparr0
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2023 chaparr0
"""

version = '1.0'

"""
with open('README.md',encoding='utf-8') as f:
    long_description = f.read()
"""

long_description = """
Add-On to markovclick module for Markov's chain with date-time koef and draw module on pygraphviz
"""

setup(
    name='markovchainswithcoef',
    version=version,

    author='chaparr0',
    author_email='madeingoa@gmail.com',

    description=long_description,
    long_description=long_description,

    url='https://github.com/chaparr0/markovchainswithcoef',

    license='Apache License, Version 2.0, see LICENSE file',

    packages=['markovchainswithcoef'],
    install_requires=['numpy','markovclick','pygraphviz','pypdf'],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ]
)