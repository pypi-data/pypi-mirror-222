from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'My Python customized module'

# Setting up
setup(
    name="VS-Python_Module",
    version=VERSION,
    author="Vishal (Vishal Singh)",
    author_email="<vskota273@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['sys'],
    keywords=['python', 'My Module'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)