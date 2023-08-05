from setuptools import setup, find_packages

setup(
    name='git-warlock',
    version='1.0.0',
    description='A script to remove .git folders in all subdirectories',
    author='willywdev',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'git-warlock=git_warlock.main:main',
        ],
    },
    install_requires=[
        'rich',  # Add any required dependencies here
    ],
)
