from distutils.core import setup

setup(
    name='email_sender',
    author='Martin Privat',
    version='0.1',
    packages=['email_sender','email_sender.tests'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description='crude email sender',
    long_description=open('README.md').read(),
    install_requires=[]
)