from re import search, MULTILINE
from setuptools import setup, find_packages


with open('aiogram3_di/_version.py') as file:
    version = search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', file.read(), MULTILINE).group(1)


with open('README.md') as file:
    long_description = file.read()


setup(
    name='aiogram3_di',
    version=version,
    url='https://github.com/Vladyslav49/aiogram3_di',
    license='MIT',
    author='Vladyslav49',
    python_requires='>=3.9',
    description='Dependency Injection implementation for aiogram 3.',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'aiogram>=3.0.0b7',
    ],
    include_package_data=False,
)
