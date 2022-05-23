# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone.formwidget.geolocation.testing import GEOLOCATION_INTEGRATION_TESTING
from Products.CMFPlone.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that plone.formwidget.geolocation is properly installed."""

    layer = GEOLOCATION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if plone.formwidget.geolocation is installed."""
        self.assertTrue(self.installer.isProductInstalled("plone.formwidget.geolocation"))


class TestUninstall(unittest.TestCase):

    layer = GEOLOCATION_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        self.installer.uninstallProducts(["plone.formwidget.geolocation"])

    def test_product_uninstalled(self):
        """Test if plone.formwidget.geolocation is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled("plone.formwidget.geolocation"))
