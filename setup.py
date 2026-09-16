from setuptools import setup

import os

version = "4.0.0.dev0"


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


setup(
    name="plone.formwidget.geolocation",
    version=version,
    description="Geolocation field and widget",
    long_description="{}\n{}".format(
        read("README.rst"),
        read("CHANGES.rst"),
    ),
    long_description_content_type="text/x-rst",
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: 6.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 5 - Production/Stable",
    ],
    keywords="z3c form leaflet map field widget",
    author="David Glick",
    author_email="dglick@gmail.com",
    url="https://github.com/collective/plone.formwidget.geolocation",
    license="GPL-2.0-or-later",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        # Plone version gate; the imported packages are listed explicitly below
        "Products.CMFPlone >= 6.1.0",
        "plone.api",
        "plone.app.registry",
        "plone.app.z3cform",
        "plone.base",
        "plone.dexterity",
        "plone.registry",
        "plone.supermodel",
        "Products.CMFCore",
        "Products.GenericSetup",
        "z3c.form",
        "Zope",
        "zope.component",
        "zope.globalrequest",
        "zope.i18n",
        "zope.i18nmessageid",
        "zope.interface",
        "zope.schema",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            # the REST API (de)serializers are only registered when
            # plone.restapi is installed
            "plone.restapi",
        ]
    },
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
