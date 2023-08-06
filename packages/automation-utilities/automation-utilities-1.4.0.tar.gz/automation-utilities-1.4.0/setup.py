from setuptools import setup

setup(
    name='automation-utilities',
    version='1.4.0',
    author='Hazem Oukal',
    description='Changed the hirarchy of the package',
    packages=['automation_utilities'],
    install_requires=['phonenumbers', 'names', 'requests', 'automation_utilities'],
)
