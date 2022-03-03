import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="idork",
    version="1.0.0",
    description="A Python library used to search content on Google and find websites with keywords.",
    long_description=(here / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author="w4ne",
    license="MIT",
    packages=find_packages(),
    install_requires=[line.strip() for line in open("requirements.txt").readlines()],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    project_urls={'GitHub': 'https://github.com/w4ne/iDork'}
)
