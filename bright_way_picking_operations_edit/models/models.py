# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockMoveInherit(models.Model):
    _inherit = "stock.move"

    cus_subtotal = fields.Float(string='Subtotal', compute='compute_cus_subtotal')

    def compute_cus_subtotal(self):
        for r in self:
            r.cus_subtotal = r.price_unit * r.product_uom_qty

# class bright_way_picking_operations_edit(models.Model):
#     _name = 'bright_way_picking_operations_edit.bright_way_picking_operations_edit'
#     _description = 'bright_way_picking_operations_edit.bright_way_picking_operations_edit'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
