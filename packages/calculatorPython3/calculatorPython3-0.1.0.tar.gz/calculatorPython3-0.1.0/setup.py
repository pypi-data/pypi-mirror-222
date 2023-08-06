from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), "r", encoding="utf-8", errors="ignore") as fh:
    long_description = fh.read()


setup(
    name='calculatorPython3',
    version='0.1.0',
    author='Jasser Abdelfattah',
    author_email='jasserabdelfattah12@gmail.com',
    description='This python calculator package for multiple calculations.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/jasserabdou/calculator-python3.git",
    packages=find_packages(),
    keywords=['python3', 'calculator'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Unix ",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    license="MIT",
    python_requires=">=3.9",
    install_requires=['numpy']
)
