from setuptools import setup, find_packages

import os, codecs, sys, re

try:
    with codecs.open( "README.md", 'r', errors='ignore' ) as file:
        readme_contents = file.read()
except Exception as error:
    readme_contents = ""
    sys.stderr.write( "Warning: Could not open README.md due %s\n" % error )
    

setup(
    name="pyTashriBS",
    author="Tashri",
    author_email="Arunthakur2342@gmail.com",
    version="0.2",
    description="This is a simple package which is used in Spam Bot",
    long_description = readme_contents,
    long_description_content_type="text/markdown",
    url="https://github.com/Tashri2342/pyTashriBS",
    packages=find_packages(),
    license="GNU General Public License v3.0",
    include_package_data=True,
    classifiers=[
        "Framework :: AsyncIO",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "Natural Language :: English",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Build Tools",

    ],
    keywords=["pyTashriBS", "TashriBS"],
    install_requires=["pyrogram", "datetime"]
)
