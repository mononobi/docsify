# -*- coding: utf-8 -*-
"""
docsify setup module.
"""

import io
import re

from setuptools import find_namespace_packages
from setuptools import setup


with io.open('README.md', 'rt', encoding='utf8') as readme_file:
    README = readme_file.read()

with io.open('src/docsify/__init__.py', 'rt', encoding='utf8') as version_file:
    VERSION = re.search(r"__version__ = '(.*?)'", version_file.read()).group(1)

PACKAGES = [
    'chardet>=3.0.4',
]

TEST_PACKAGES = PACKAGES + [
    'pytest',
    'pytest-cov',
    'pygments',
]

setup(
    name='docsify',
    version=VERSION,
    url='https://github.com/mononobi/docsify',
    project_urls={
        'Code': 'https://github.com/mononobi/docsify',
        'Issue tracker': 'https://github.com/mononobi/docsify/issues',
    },
    license='GPL-3.0',
    author='Mohamad Nobakht',
    author_email='mohamadnobakht@gmail.com',
    maintainer='Mohamad Nobakht',
    maintainer_email='mohamadnobakht@gmail.com',
    description='A simple docstring inspector.',
    long_description=README,
    long_description_content_type='text/markdown',
    keywords='docsify python docstring inspector extractor swagger '
             'converter re-structured',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    packages=find_namespace_packages('src', exclude=('tests', 'tests.*')),
    package_dir={'': 'src'},
    package_data={'': ['*']},
    include_package_data=True,
    python_requires='>=3.5',
    install_requires=PACKAGES,
    extras_require={
        'tests': TEST_PACKAGES,
    },
    # entry_points={"console_scripts": ["docsify = docsify.cli.manager:main"]},
)
