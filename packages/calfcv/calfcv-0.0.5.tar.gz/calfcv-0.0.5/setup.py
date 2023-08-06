#! /usr/bin/env python
""" The calfcv package setup file.

To build and upload a new distribution
1.  Update the version

2. cd to calfcv and build the dist folder with
python setup.py sdist bdist_wheel

3. twine upload dist/*

"""

import codecs
import os

from setuptools import find_packages, setup

# get __version__ from _version.py
ver_file = os.path.join('calfcv', '_version.py')
with open(ver_file) as f:
    exec(f.read())

DISTNAME = 'calfcv'
DESCRIPTION = 'Coarse approximation linear function with cross validation'
with codecs.open('README.rst', encoding='utf-8-sig') as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = 'Carlson Research, LLC'
MAINTAINER_EMAIL = 'hrolfrc@gmail.com'
URL = ''
LICENSE = 'new BSD'
DOWNLOAD_URL = 'https://github.com/scikit-learn-contrib/project-template'
VERSION = '0.0.5'
INSTALL_REQUIRES = ['numpy', 'scipy', 'scikit-learn']
CLASSIFIERS = ['Intended Audience :: Science/Research',
               'Intended Audience :: Developers',
               'Development Status :: 2 - Pre-Alpha',
               'License :: OSI Approved',
               'Topic :: Scientific/Engineering',
               'Operating System :: OS Independent',
               'Programming Language :: Python :: 3']

# EXTRAS_REQUIRE = {
#     'tests': [
#         'pytest',
#         'pytest-cov'],
#     'docs': [
#         'sphinx',
#         'sphinx-gallery',
#         'sphinx_rtd_theme',
#         'numpydoc',
#         'matplotlib'
#     ]
# }

setup(name=DISTNAME,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      description=DESCRIPTION,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      long_description=LONG_DESCRIPTION,
      zip_safe=False,  # the package can run out of an .egg file
      classifiers=CLASSIFIERS,
      packages=find_packages(),
      install_requires=INSTALL_REQUIRES)  # ,
# extras_require=EXTRAS_REQUIRE)
