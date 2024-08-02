from setuptools import setup, find_packages

def parse_requirements(filename):
    """ Load requirements from a pip requirements file """
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name='optionsValuation',
    version='0.1.0',
    packages=find_packages(),
    install_requires=parse_requirements('./requirements.txt'),
    author='Anurag',
    description='Obtain Options Valuations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AnuragChaudhari7/optionsValuationAPI',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)