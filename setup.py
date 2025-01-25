import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(_file_).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Topsis_Miet_102203012",
    version="1.0.0",
    description="Multiple Criteria Decision Making using Topsis",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/uditvashisht/saral-square",
    author="Udit Vashisht",
    author_email="admin@saralgyaan.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["square"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "square=square._main_:main",
        ]
    },
)