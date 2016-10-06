# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '2.0'

setup(
    name='plone.formwidget.geolocation',
    version=version,
    description="Geolocation field and widget",
    long_description="{0}\n{1}".format(
        open("README.rst").read(),
        open("CHANGES.rst").read()
    ),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
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
