# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class nakham_invoice_report_inherit(models.Model):
#     _name = 'nakham_invoice_report_inherit.nakham_invoice_report_inherit'
#     _description = 'nakham_invoice_report_inherit.nakham_invoice_report_inherit'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
