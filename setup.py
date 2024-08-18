# Importing Packages
from importlib.util import module_from_spec, spec_from_file_location
from setuptools import find_packages, setup

# Reading `README` and Storing Info as `Long Description`
with open('README.md', 'r') as fh:
    longDescription: str = fh.read()

# Reading `version` from `version.py` without Importing [as it causes circular imports]
specs: spec_from_file_location = spec_from_file_location(name='version', location='directory_tree/version.py')
versionModule: module_from_spec = module_from_spec(spec=specs)
specs.loader.exec_module(module=versionModule)

# Configuring Setup
setup(

    # Package and Author Information
    name='directory_tree',
    version=versionModule.__version__,
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
    py_modules=['directory_tree'],
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
