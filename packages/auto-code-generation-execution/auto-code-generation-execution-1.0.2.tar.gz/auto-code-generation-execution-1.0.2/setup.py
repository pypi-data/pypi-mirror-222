
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name="auto-code-generation-execution",
    version="1.0.2",
    packages=find_packages(),
    py_modules=['auto_code_generation_execution'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'auto_code_generation_execution = auto_code_generation_execution:main',
        ],
    },
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',)
