# -*- coding: utf-8 -*-

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
        self.assertTrue(
            self.installer.is_product_installed("plone.formwidget.geolocation")
        )


class TestUninstall(unittest.TestCase):

    layer = GEOLOCATION_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        self.installer.uninstall_product("plone.formwidget.geolocation")

    def test_product_uninstalled(self):
        """Test if plone.formwidget.geolocation is cleanly uninstalled."""
        self.assertFalse(
            self.installer.is_product_installed("plone.formwidget.geolocation")
        )
