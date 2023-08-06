from setuptools import setup, find_packages

setup(
    name='anakin',
    version='1.0.1',
    description='Anakin Command Line Utility',
    long_description='Add a long description here if you want.',
    author='z10mx7',
    author_email='z10mx7@protonmail.com',
    url='https://github.com/z10mx7/anakin',   
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'anakin = anakin:main',
        ],
    },
    install_requires=[
        'colorama',  # Add any dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
