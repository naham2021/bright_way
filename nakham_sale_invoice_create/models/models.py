# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    def create_invoices_and_open(self):
        self._create_invoices(final=True)
        return self.action_view_invoice()

    # For Migration Errors
    terms_ar = fields.Char()
    terms_en = fields.Char()
    warranty = fields.Char()
    payment_id = fields.Many2one('account.payment')
    bank_account = fields.Char()
    delivery_set = fields.Char()
    margin = fields.Char()
