from setuptools import setup, find_packages

setup(
    name='docsbot',
    version='0.1.0',
    description='A simple chat bot for querying information from your local private documents.',
    author='DataMini',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'docsbot = cli:main',
        ]
    }
)