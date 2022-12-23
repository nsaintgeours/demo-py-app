from setuptools import find_packages, setup

setup(
    name='backend',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    version='0.0.1',
    description='Backend REST API for the DemoPyApp project.',
    author='',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    include_package_data=True
)
