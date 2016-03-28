mport codecs
import os
import re

from setuptools import setup, find_packages


###################################################################

NAME = "pytosms"
PACKAGES = find_packages(where="src")
META_PATH = os.path.join("src", "pytosms", "__init__.py")
KEYWORDS = ["class", "sms", "messaging"]
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Topic :: Software Development :: Libraries :: Python Modules"]

INSTALL_REQUIRES = []

##################################################################

HERE = os.path.abspath(os.path.dirname(__file__))

def read(*parts):

    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()
