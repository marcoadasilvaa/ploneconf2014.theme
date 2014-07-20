# -*- coding: utf-8 -*-

"""
This is an integration "unit" test.
"""

import unittest

from plone import api
from plone.browserlayer.utils import registered_layers
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from ploneconf2014.theme.config import PROJECTNAME, DEPENDENCIES
from ploneconf2014.theme.testing import INTEGRATION_TESTING
from ploneconf2014.theme.interfaces import ICustomTheme

class InstallTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = api.portal.get_tool(name='portal_quickinstaller')

    def test_installed(self):
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME))

    def test_addon_layer(self):
        """
        This method test if the ICustomTheme is available.
        """
        layers = [l.getName() for l in registered_layers()]
        self.assertTrue('ICustomTheme' in layers,
                        'add-on layer was not installed')

class UninstallTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.qi = getattr(self.portal, 'portal_quickinstaller')
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))