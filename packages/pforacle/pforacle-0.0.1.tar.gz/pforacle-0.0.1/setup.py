from setuptools import find_packages, setup

PACKAGE_NAME = "pforacle"

setup(
    name="pforacle",
    version="0.0.1",
    description="This package contains promptflow tools to query Oracle databases to assist in grounded LLM responses",
    packages=find_packages(),
    entry_points={
        "package_tools": ["query = oracle.tools.utils:list_package_tools"],
    },
    include_package_data=True,   # This line tells setuptools to include files from MANIFEST.in
)