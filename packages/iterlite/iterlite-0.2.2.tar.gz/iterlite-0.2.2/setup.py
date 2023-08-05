from setuptools import setup
from iterlite import __version__

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='iterlite',
    version=__version__,    
    description='rust like iterators for python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/peturparkur/python-rustlite',
    author='Peter Nagymathe',
    author_email='peter@nagymathe.xyz',
    license='AGPLv3+',
    packages=['iterlite'],
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed"
    ]
)
