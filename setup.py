from setuptools import setup, find_packages
import sys

install_requires = ["python-magic-bin", "pathspec"]

setup(
    name="folder2text",
    version="0.1",
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "folder2text = src.combine_files:main",
        ],
    },
)