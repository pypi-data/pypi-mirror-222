from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="LYNKPY",
    version="0.0.1",
    author="Siddharth",
    author_email="ssiddharth408@gmail.com",
    description="basic utilities",
    long_description="basic utilities",
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)