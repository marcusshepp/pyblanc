"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
from setuptools import setup

setup(
    name='pyblanc',
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.1',
    description='League of Legends API wrapper.',
    url='https://github.com/marcusshepp/PyBlanc',
    # Author details
    author='Marcus Shepherd',
    author_email='sheph2mj@cmich.edu',
    license=None,
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='',
    install_requires=[
        'numpy',
        'requests',
        'requests_cache',
    ],
)