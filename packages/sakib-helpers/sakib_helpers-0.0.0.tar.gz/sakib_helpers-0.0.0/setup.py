from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.0'
DESCRIPTION = 'python helper functions/methods'
LONG_DESCRIPTION = 'In this package have more helpful packages used in django and python. This package is developed by sakib malik.'

# Setting up
setup(
    name="sakib_helpers",
    version=VERSION,
    author="Sakib Malik",
    author_email="maliksakib347@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['arithmetic', 'math', 'mathematics',
              'python tutorial'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
