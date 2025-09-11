from pathlib import Path
from setuptools import find_packages
from setuptools import setup


version = "3.0.8.dev0"


setup(
    name="plone.formwidget.geolocation",
    version=version,
    description="Geolocation field and widget",
    long_description=(
        f"{Path('README.rst').read_text()}\n{Path('CHANGES.rst').read_text()}\n"
    ),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="z3c form leaflet map field widget",
    author="David Glick",
    author_email="dglick@gmail.com",
    url="https://github.com/collective/plone.formwidget.geolocation",
    license="GPL",
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["plone", "plone.formwidget"],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "setuptools",
        "z3c.form",
        "Products.CMFPlone >= 6.0.0",
        "plone.api",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "plone.restapi",
            "plone.testing",
            "mock",
        ]
    },
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
