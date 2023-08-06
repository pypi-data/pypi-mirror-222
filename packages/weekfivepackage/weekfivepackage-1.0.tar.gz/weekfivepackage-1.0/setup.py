from setuptools import setup, find_packages

setup(
    name="weekfivepackage",
    author="Ajit Shrestha",
    description="This is a weekfivepackage.",
    long_description="This is a weekfivepackage that has codes from week 2 to week 4.",
    version="1.0",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    author_email="ajitstha16@gmail.com",
)
