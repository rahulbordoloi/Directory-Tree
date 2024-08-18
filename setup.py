# Importing Packages
from setuptools import find_packages, setup
from directory_tree.version import __version__

# Reading README and Storing Info as `Long Description`
with open('README.md', 'r') as fh:
    longDescription: str = fh.read()

# Configuring Setup
setup(

    # Package and Author Information
    name='directory_tree',
    version=__version__,
    description='Utility Package that Displays out the Tree Structure of a Particular Directory.',
    url='https://github.com/rahulbordoloi/Directory-Tree/',
    author='Rahul Bordoloi',
    author_email='rahulbordoloi24@gmail.com',

    # Package Information
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'directory_tree=directory_tree.__main__:directoryTreeCli',
        ]
    },
    package_dir={'directory_tree': 'directory_tree'},

    # Package Dependencies
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Utilities',
        'Natural Language :: English',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Customer Service',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop'
    ],

    # Package Description
    long_description=longDescription,
    long_description_content_type='text/markdown',

    # Package Requirements [Extra]
    extras_require={
        'dev': [
            'pytest >= 3.7',
        ],
    }
)
