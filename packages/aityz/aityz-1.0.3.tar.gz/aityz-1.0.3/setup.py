from setuptools import setup, find_packages

setup(
    name='aityz',
    version='1.0.3',
    packages=find_packages(),
    install_requires=[
        'rsa',
        'pycryptodome'
    ],
    author='Aityz',
    author_email='itzaityz@gmail.com',
    description='The multipurpose package, built for programmers',
    long_description='Aityz Library is a multipurpose library made for many different use cases for Python. From '
                     'Machine Learning to Encryption, it has simplified many different ways of using Python.',
    url='https://github.com/Aityz/Library',
)
