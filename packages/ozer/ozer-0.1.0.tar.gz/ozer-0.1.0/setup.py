from setuptools import setup, find_packages

setup(
    name='ozer',
    version='0.1.0',
    description='Output analyzer',
    author='Ehsan Shirzadi',
    packages=find_packages(),
    install_requires=[
        # List any dependencies your library needs
        'yaml'
    ],
)
