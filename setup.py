##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for zope.lifecycleevent package

$Id$
"""

import os

from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('src', 'zope', 'lifecycleevent', 'README.txt')
    + '\n' +
    'Download\n'
    '********\n'
    )

setup(
    name='zope.lifecycleevent',
    version='3.5.0',
    url='http://pypi.python.org/pypi/zope.lifecycleevent',
    author='Zope Corporation and Contributors',
    author_email='zope3-dev@zope.org',
    license='ZPL 2.1',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        ],
    description='Life-cycle events',
    long_description=long_description,

    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['zope',],
    include_package_data=True,
    install_requires=['setuptools',
                      'zope.interface',
                      'zope.component',
                      'zope.deferredimport',
                      'zope.event'],
    extras_require=dict(
        test = ['zope.annotation',
                'zope.dublincore',
                'zope.container',]
        ),
    zip_safe=False,
    )
