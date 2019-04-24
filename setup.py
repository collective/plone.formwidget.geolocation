# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

import os

version = '2.2.0'


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


setup(
    name='plone.formwidget.geolocation',
    version=version,
    description="Geolocation field and widget",
    long_description="{0}\n{1}".format(
        read("README.rst"),
        read("CHANGES.rst"),
    ),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='',
    author='David Glick',
    author_email='dglick@gmail.com',
    url='https://github.com/collective/plone.formwidget.geolocation',
    license='GPL',
    packages=find_packages(),
    namespace_packages=['plone', 'plone.formwidget'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.patternslib',
        'setuptools',
        'z3c.form',
    ],
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
