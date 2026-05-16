from setuptools import setup, find_packages

setup(
    name="textilecalc",
    version="1.0.0",
    author="Abdul Malek",
    description="A complete textile engineering calculation library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.7",
)