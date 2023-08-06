from setuptools import setup, find_packages

# Read the long description from README.md
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

version = "0.0.10"

setup(
    name='pygenlib',
    version=version,
    description='A Python library for generating other Python libraries',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers'
    ],
    packages=find_packages(),
    package_data={
        'pygenlib': ['templates/*'],
    },
    entry_points={
        'console_scripts': [
            'pygenlib = pygenlib.create_library_template:main'
        ]
    },
)
