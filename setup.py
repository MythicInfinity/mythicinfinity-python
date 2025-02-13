from __future__ import absolute_import
from __future__ import print_function

import io
import os
import re
from os.path import dirname
from os.path import join

from setuptools import find_packages
from setuptools import setup

this_file_dir = os.path.dirname(
    os.path.abspath(
        os.path.realpath(__file__)))


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__\s*=\s*['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name='mythicinfinity',
    version=find_version(this_file_dir, "mythicinfinity", "__version__.py"),
    license='MIT',
    description='Mythic Infinity python client library.',

    long_description=read(os.path.join(this_file_dir, "README.md")),
    long_description_content_type='text/markdown',

    author='Mythic Infinity',

    url='https://www.mythicinfinity.com/',
    project_urls={
        'Repository': 'https://github.com/mythicinfinity/mythicinfinity-python',
    },

    install_requires=[
        "httpx >= 0.21.2",
        "pydantic >= 1.9.2",
        "pydantic-core >= 2.18.2,==2.*",
        "typing_extensions >= 4.0.0",
    ],
    extras_require={"test": [
        "pytest==8.3.4",
        "pytest-xdist==3.6.1",
        "pytest-asyncio==0.24.0",
    ]},

    python_requires=">=3.8",

    packages=find_packages(exclude=["test", ".github"]),
    zip_safe=False,

    include_package_data=True,

    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
        "License :: OSI Approved :: MIT License"
    ]
)
