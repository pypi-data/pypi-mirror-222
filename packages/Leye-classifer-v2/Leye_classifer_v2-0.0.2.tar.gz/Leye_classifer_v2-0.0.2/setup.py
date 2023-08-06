import pathlib
from setuptools import setup, find_packages

setup(
    name='Leye_classifer_v2',
    version='0.0.2',
    author='Bayode Ogunleye',
    author_email='batoog101@yahoo.com',
    description='A sentiment lexicon algorithm to classify pidgin English and English text into positive, negative or neutral',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/batoog101/SentiLEYE.git',
    
    packages=find_packages(where='sentileye'),
    package_dir={"": "sentileye"},
    include_package_data=True,
    
    keywords=['sentiment analysis', 'pidgin', 'bank'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)

