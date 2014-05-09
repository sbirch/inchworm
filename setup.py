from setuptools import setup

setup(name='inchworm',
    version='0.1',
    description='A small Python module for progress bars in IPython',
    url='',
    author='Sam Birch',
    author_email='sam.m.birch@gmail.com',
    license='MIT',
    packages=['inchworm'],
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'])