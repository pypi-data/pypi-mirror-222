# pygenlib/templates/setup_template.py

from setuptools import setup

version = "1.0.0"

setup(
    name='{library_name}',
    version=version,
    description='A brief description of your library',
    author='Your Name',
    author_email='your.email@example.com',
    packages=['{library_name}', '{library_name}.{library_name}_utils'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.x',
    ],
)