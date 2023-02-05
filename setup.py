from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(

    name = 'directory_tree',
    version = '0.0.3',
    description = 'Utility Package that displays out the Tree Structure of a Particular Directory.',
    url = "https://github.com/rahulbordoloi/Directory-Tree/",
    author = "Rahul Bordoloi",
    author_email = "rahulbordoloi24@gmail.com",

    py_modules = ['directory_tree'],
    package_dir = {'': 'src'},

    classifiers = [
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Utilities",
        "Natural Language :: English",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Customer Service",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop"
    ],

    long_description = long_description,
    long_description_content_type = "text/markdown",

    extras_require = {
        "dev" : [
            "pytest >= 3.7",
        ],
    },
)
