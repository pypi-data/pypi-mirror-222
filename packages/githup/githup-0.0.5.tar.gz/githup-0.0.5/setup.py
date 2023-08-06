from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.5'
DESCRIPTION = 'Upload files on GitHub using Python'
LONG_DESCRIPTION = 'download/initiate/commit new repositories and create files to upload them on GitHub using Python'

# Setting up
setup(
    name="githup",
    version=VERSION,
    author="Cyril Frébel",
    author_email="cyril.frebel@proton.me",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'upload', 'github', 'files'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)