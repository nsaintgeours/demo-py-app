from setuptools import find_packages, setup

setup(
    name='frontend',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    version='0.0.1',
    description='Frontend for the DemoPyApp project.',
    author='',
    license='GNU GENERAL PUBLIC LICENSE Version 3'
)
