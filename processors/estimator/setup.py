import os
from setuptools import setup, find_packages


# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "sentiment_estimator",
    version = "0.0.1",
    author = "Orel Balilti",
    author_email = "orel.balilti@gmail.com",
    description = ("A way to estimate sentiment based on articles "),
    license = "BSD",
    keywords = "",
    packages=["spacy"],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: NLP",
        "Environment :: Console",
        "License :: OSI Approved :: BSD License",
    ],
)