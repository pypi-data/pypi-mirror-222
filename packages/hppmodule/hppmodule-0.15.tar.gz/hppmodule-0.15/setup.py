from setuptools import setup
setup(name='hppmodule',
version='0.15',
description='Testing installation of Package',
author='Pa Pa',
author_email='htunpa2aung@gmail.com',
license='MIT',
packages=['mypackage'],
install_requires=[
    'requests',
    'flask',
],
zip_safe=False)