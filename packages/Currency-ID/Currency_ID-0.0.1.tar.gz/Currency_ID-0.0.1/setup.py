from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Currency_ID'
LONG_DESCRIPTION = 'A package to give the Country Currency ID'

# Setting up
setup(
    name="Currency_ID",
    version=VERSION,
    author="Jagadeeswarudu Kattubadi",
    author_email="jagat0963@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['CurrencyConverter', 'math', 'mathematics', 'python tutorial', 'Currency_ID'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)