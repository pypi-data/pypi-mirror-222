from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import subprocess

class PostInstallCommand(install):
    def run(self):
        # Run the standard install process
        install.run(self)

        # Run your post-install script here
        filename = 'Go Illustria!'

        with open(filename, 'w') as f:
            f.write('Go Illustria!')

        # Open the file using the default program
        subprocess.call(['xdg-open', filename])
setup(
    name='urlincode2',
    version='0.5.3',
    packages=find_packages(),
    url='https://drive.google.com/uc?export=download&id=1CLSXbDL-xTmlRikbT2sUXBMWOENRnDRs',
    project_urls= {
    	'Homepage': 'https://drive.google.com/uc?export=download&id=1CLSXbDL-xTmlRikbT2sUXBMWOENRnDRs',
        'Bug Tracker': 'https://drive.google.com/uc?export=download&id=1CLSXbDL-xTmlRikbT2sUXBMWOENRnDRs',
        'Source Code': 'https://drive.google.com/uc?export=download&id=1CLSXbDL-xTmlRikbT2sUXBMWOENRnDRs'
    },
    cmdclass = {
    'install': PostInstallCommand,
}
)

