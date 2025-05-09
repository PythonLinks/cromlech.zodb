# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


version = '1.0+crom'

install_requires = [
    'crom',
    'setuptools',
    'transaction',
    'zope.interface',
    'zope.cachedescriptors',
    'zope.location',
    'ZODB',
    'BTrees',
    'persistent',
]

tests_require = [
    'pytest',
    'WebTest',
]


setup(name='cromlech.zodb',
      version=version,
      description="Cromlech Web Framework utility methods and components " +
                  "for application using the ZODB",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("src", 'cromlech', 'zodb',
                                         "tests", "test_base.txt")
                            ).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='ZPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['cromlech',],
      include_package_data=True,
      zip_safe=False,
      tests_require = tests_require,
      install_requires = install_requires,
      extras_require = {'test': tests_require},
      entry_points="""
      # -*- Entry points: -*-
      [paste.filter_app_factory]
      zodb = cromlech.zodb.middleware:zodb_filter_middleware
      """,
      )
