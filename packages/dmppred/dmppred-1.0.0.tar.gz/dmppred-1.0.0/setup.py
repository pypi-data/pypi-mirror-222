# setup.py

from setuptools import setup, find_packages
setup(
    name='dmppred',
    version='1.0.0',
    description='Dmppred: A tool for predicting, designing, and scanning Type 1 associated peptides',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Nishant Kumar',
    author_email='nishantk@iiitd.ac.in',
    url='https://gitlab.com/raghavalab/dmppred',
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        # Add other classifiers as needed
    ],
    package_data={'dmppred': ['model/*']},
)

