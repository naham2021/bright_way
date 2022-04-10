# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMoveLineInherit(models.Model):
    _inherit = 'account.move.line'

    related_product_category = fields.Many2one(string='Product Category', related='product_id.categ_id')


# class bright_way_journal_fields(models.Model):
#     _name = 'bright_way_journal_fields.bright_way_journal_fields'
#     _description = 'bright_way_journal_fields.bright_way_journal_fields'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
