from setuptools import setup, find_packages

import os
import sys
from setuptools.command.install import install
import atexit


def run_post_install():
    # Replace 'install.sh' with the name of your .sh file
    post_install_script = os.path.join(sys.prefix, 'bin', 'install.sh')
    os.system(f'bash {post_install_script}')


class CustomInstall(install):
    def run(self):
        install.run(self)
        atexit.register(run_post_install)


setup(
    name='ozer',
    version='0.1.1',
    description='Output analyzer',
    author='Ehsan Shirzadi',
    packages=find_packages(),
    install_requires=[
        # List any dependencies your library needs
        'PyYAML'
    ],
    cmdclass={
        'install': CustomInstall,
    }
)
