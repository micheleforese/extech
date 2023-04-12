from pathlib import Path

from setuptools import find_packages, setup

version = "0.0.1"
setup(
    name="Extech Light Meter",
    version=version,
    description="Extech Light Meter",
    long_description=Path("README.md").read_text(),
    author="Michele Forese",
    author_email="michele.forese.personal@gmail.com",
    url="https://github.com/micheleforesedev/extech",
    packages=find_packages(include=["extech"]),
    install_requires=Path("requirements.txt").read_text().splitlines(),
)
