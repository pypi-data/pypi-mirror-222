#
#   Function
#   Copyright © 2023 NatML Inc. All Rights Reserved.
#

from setuptools import find_packages, setup

# Get readme
with open("README.md", "r") as readme:
    long_description = readme.read()

# Get version
with open("edgefxn/version.py") as version_source:
    gvars = {}
    exec(version_source.read(), gvars)
    version = gvars["__version__"]

# Setup
setup(
    name="edgefxn",
    version=version,
    author="NatML Inc.",
    author_email="hi@fxn.ai",
    description="AI prediction functions at the edge.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    python_requires=">=3.7",
    install_requires=[
        "fxn"
    ],
    url="https://fxn.ai",
    packages=find_packages(
        include=["edgefxn", "edgefxn.*"],
        exclude=["test"]
    ),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Software Development :: Libraries",
    ],
    project_urls={
        "Documentation": "https://docs.fxn.ai",
        "Source": "https://github.com/fxnai/edgefxn"
    },
)