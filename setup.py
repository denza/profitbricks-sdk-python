#!/usr/bin/python3

# Copyright 2015-2017 ProfitBricks GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Setup script for the ProfitBricks API Python client.

"""
from __future__ import print_function

import codecs
import os
import re
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


if os.path.isfile("README.md"):
    long_desc = read('README.md')
else:
    long_desc = "ProfitBricks API Client Library for Python"


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--strict', '--verbose', '--tb=long', 'tests']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='profitbricks',
    version=find_version('profitbricks', '__init__.py'),
    description='ProfitBricks API Client Library for Python',
    long_description=long_desc,
    author='Matt Baldwin (stackpointcloud.com)',
    author_email='baldwin@stackpointcloud.com',
    url='https://github.com/profitbricks/profitbricks-sdk-python',
    install_requires=['requests>=2.0.0', 'six>=1.10.0'],
    packages=['profitbricks'],
    platforms='any',
    test_suite='profitbricks.test.test_profitbricks',
    cmdclass={'test': PyTest},
    tests_require=['pytest'],
    license='Apache 2.0',
    keywords='profitbricks api client cloud',
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Natural Language :: English',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: Apache Software License',
                 'Operating System :: POSIX',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 3',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'Topic :: Software Development :: Libraries :: Application Frameworks',
                 'Topic :: Internet :: WWW/HTTP'],
    extras_require={
        'testing': ['pytest'],
    }
)
