# This file is part stock_shipment_shop module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['ShipmentOut', 'ShipmentOutReturn']
__metaclass__ = PoolMeta


class ShipmentOut:
    __name__ = 'stock.shipment.out'
    shop = fields.Function(fields.Many2One('sale.shop', 'Shop'),
        'get_shop')

    def get_shop(self, name):
        if not self.origin:
            return None
        origin = self.origin
        if hasattr(origin, 'shop'):
            shop = getattr(origin, 'shop')
            if shop:
                return shop.id
        return None


class ShipmentOutReturn:
    __name__ = 'stock.shipment.out.return'
    shop = fields.Function(fields.Many2One('sale.shop', 'Shop'),
        'get_shop')

    def get_shop(self, name):
        if not self.origin:
            return None
        origin = self.origin
        if hasattr(origin, 'shop'):
            shop = getattr(origin, 'shop')
            if shop:
                return shop.id
        return None
