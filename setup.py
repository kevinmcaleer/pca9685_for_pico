import pathlib
from setuptools import setup

# The directory contaoining this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pca9685_for_pico",
    version="1.0.0",
    description="PCA9685 for Raspberry Pi Pico",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/kevinmcaleer/smars_library",
    author="Kevin McAleer",
    author_email="kevinmcaleer@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["smars_library"],
    include_package_data=False,
    install_requires=["adafruit-pca9685","pathlib"],
    )