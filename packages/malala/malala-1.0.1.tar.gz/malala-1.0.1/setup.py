from setuptools import setup, find_packages

with open("requirements.txt", "r") as file:
    dependencies = file.readlines()

with open("README.md", "r", encoding="utf-8") as file:
    readme = file.read()

setup(
    name="malala",
    version="1.0.1",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[dep.strip() for dep in dependencies],
    long_description=readme,
    long_description_content_type="text/markdown",
)
