from setuptools import setup, find_packages

setup(
    name='docsbot',
    version='0.1.1',
    description='A simple chat bot for querying information from your local private documents.',
    author='J',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'docsbot = cli:main',
        ]
    }
)