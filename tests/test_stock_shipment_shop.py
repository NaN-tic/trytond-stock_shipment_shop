# This file is part of the stock_shipment_shop module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class StockShipmentShopTestCase(ModuleTestCase):
    'Test Stock Shipment Shop module'
    module = 'stock_shipment_shop'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockShipmentShopTestCase))
    return suite