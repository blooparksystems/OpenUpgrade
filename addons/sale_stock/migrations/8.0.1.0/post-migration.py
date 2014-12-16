# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, a suite of business apps
#    This module Copyright (C) 2014 Therp BV (<http://therp.nl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.modules.registry import RegistryManager
from openerp.openupgrade import openupgrade
from openerp import SUPERUSER_ID

possible_dataloss_fields = [
    {
        'table': 'sale_order_line_property_rel',
        'field': 'order_id', 'new_module': 'sale_mrp',
    },
    {
        'table': 'sale_order_line_property_rel',
        'field': 'property_id', 'new_module': 'sale_mrp',
    }
]


def migrate_warehouse_id(cr, pool, uid):
    # get transition ids for sale_stock to disable them
    data_obj = pool.get("ir.model.data")
    disable_transitions = [
        ('sale_stock', 'trans_ship_ship_except'),
        ('sale_stock', 'trans_ship_ship_end'),
        ('sale_stock', 'trans_wait_ship_ship'),
        ('sale_stock', 'trans_ship_except_ship'),
        ('sale_stock', 'trans_router_wait_ship'),
        ('sale_stock', 'trans_router_wait_invoice_shipping'),
        ('sale_stock', 'trans_wait_invoice_invoice'),
        ('sale_stock', 'trans_wait_ship_cancel3a'),
        ('sale_stock', 'trans_ship_end_done'),
        ('sale_stock', 'trans_ship_except_ship_end'),
        ('sale_stock', 'trans_ship_except_ship_cancel'),
    ]
    transition_conditions = {}
    for module, name in disable_transitions:
        try:
            transition_id = data_obj.get_object_reference(
            cr, SUPERUSER_ID, module, name)[1]
            transition_conditions[transition_id] = None
        except ValueError:
            continue

    # backup values
    cr.execute(
        "SELECT id, condition FROM wkf_transition WHERE id in %s",
        (tuple(transition_conditions.keys()),))
    transition_conditions = dict(cr.fetchall())

    # disabling transitions during 'sale_order' update.
    cr.execute(
        "UPDATE wkf_transition SET condition = 'False' WHERE id in %s",
        (tuple(transition_conditions.keys()),))

    cr.execute(
        '''update sale_order so set warehouse_id=ss.warehouse_id
        from sale_shop ss where so.shop_id=ss.id''')

    # Rewriting good values
    for transition_id, condition in transition_conditions.iteritems():
        cr.execute(
            "update wkf_transition set condition = %s where id=%s",
            (condition, transition_id))

@openupgrade.migrate()
def migrate(cr, version):
    pool = RegistryManager.get(cr.dbname)

    migrate_warehouse_id(cr)
    openupgrade.delete_model_workflow(cr, 'sale.shop')
    openupgrade.warn_possible_dataloss(
        cr, pool, 'sale_stock', possible_dataloss_fields)

    openupgrade.m2o_to_x2m(
        cr, pool['sale.order.line'], 'sale_order_line', 'procurement_ids',
        openupgrade.get_legacy_name('procurement_id')
    )
