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

setup(name='zope.lifecycleevent',
      version = '3.4.0b1',
      url='http://svn.zope.org/zope.lifecycleevent',
      license='ZPL 2.1',
      description='Zope lifecycleevent',
      author='Zope Corporation and Contributors',
      author_email='zope3-dev@zope.org',
      long_description="In Zope 3, events are used by components"
                        "to inform each other about relevant new"
                        "objects and object modifications.",

      packages=find_packages('src'),
      package_dir = {'': 'src'},

      namespace_packages=['zope',],
      tests_require = ['zope.testing'],
      install_requires=['setuptools',
                        'zope.interface',
                        'zope.component',
                        'zope.deferredimport',
                        'zope.event'],
      include_package_data = True,

      zip_safe = False,
      extras_require = dict(
        test = ['zope.annotation',
                'zope.app.container',
               ]
        )
      )
