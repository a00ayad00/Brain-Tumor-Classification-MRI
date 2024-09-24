import setuptools
from src import logger

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()  # If you want to publish this on PyPi


__version__ = '0.1'
ProjectName = "BrainTumorClassification"
AuthorUserName = "a00ayad00"
AuthorEmail = "3bdullah3yad@gmail.com"
RepoName = "Brain-Tumor-Classification-MRI"

setuptools.setup(
    name=ProjectName,
    version=__version__,
    author=AuthorUserName,
    author_email=AuthorEmail,
    description="A small python package for CNN app to classify brain tumors",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AuthorUserName}/{RepoName}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AuthorUserName}/{RepoName}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)