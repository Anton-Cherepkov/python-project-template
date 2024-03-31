# -*- coding: utf-8 -*-
import io
from typing import List

from setuptools import find_packages, setup

with io.open("requirements.in", "r", encoding="utf-8") as req_file:
    requirements: List[str] = req_file.read().splitlines()


setup(
    name="antons-solution",
    author="Anton Cherepkov",
    version="0.0.1",
    packages=find_packages(exclude=["tests", "scripts"]),
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.11",
    classifiers=[
        "Development Status :: 1 - Beta",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Natural Language :: English",
        "License :: Checklens",
        "Operating System :: OS Independent",
    ],
)
