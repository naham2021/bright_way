# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, tools
import logging

_logger = logging.getLogger(__name__)

try:
    from num2words import num2words
except ImportError:
    _logger.warning("The num2words python library is not installed, amount-to-text features won't be fully available.")
    num2words = None


class ResCurrencyInherit(models.Model):
    _inherit = 'res.currency'

    def ar_amount_to_text(self, amount):
        self.ensure_one()

        def _num2words(number, lang):
            return num2words(number, lang=lang).title()

        if num2words is None:
            logging.getLogger(__name__).warning("The library 'num2words' is missing, cannot render textual amounts.")
            return ""

        formatted = "%.{0}f".format(self.decimal_places) % amount
        parts = formatted.partition('.')
        integer_value = int(parts[0])
        fractional_value = int(parts[2] or 0)

        # lang_code = 'ar_SY'
        # lang = self.env['res.lang'].with_context(active_test=False).search([('code', '=', lang_code)])
        amount_words = tools.ustr('{amt_value} {amt_word}').format(
            amt_value=num2words(integer_value, lang='ar'),
            amt_word='' if self.is_zero(amount - integer_value) else '',
            # 'جنيه مصرى لا غير'
            # 'جنيها'
        )
        if not self.is_zero(amount - integer_value):
            amount_words += ' ' + _('و') + tools.ustr(' {amt_value} {amt_word}').format(
                amt_value=num2words(fractional_value, lang='ar'),
                amt_word='' if fractional_value > 10 else '',
                # 'قرش مصرى لا غير'
                # 'قروش فقط لا غير '
            )
        return amount_words

    def amount_to_text(self, amount):
        self.ensure_one()

        def _num2words(number, lang):
            return num2words(number, lang=lang).title()

        if num2words is None:
            logging.getLogger(__name__).warning(
                "The library 'num2words' is missing, cannot render textual amounts.")
            return ""

        formatted = "%.{0}f".format(self.decimal_places) % amount
        parts = formatted.partition('.')
        integer_value = int(parts[0])
        fractional_value = int(parts[2] or 0)

        lang_code = 'en_US'
        lang = self.env['res.lang'].with_context(active_test=False).search([('code', '=', lang_code)])

        amount_words = tools.ustr('{amt_value} {amt_word}').format(
            amt_value=_num2words(integer_value, lang=lang.iso_code),
            amt_word='Riyal' if self.is_zero(amount - integer_value) else 'Riyal',
        )
        if not self.is_zero(amount - integer_value):
            amount_words += ' ' + _('and') + tools.ustr(' {amt_value} {amt_word}').format(
                amt_value=_num2words(fractional_value, lang=lang.iso_code),
                amt_word='Halala' if fractional_value > 10 else 'Halala',
            )
        return amount_words

# class bright_way_vat_invoice(models.Model):
#     _name = 'bright_way_vat_invoice.bright_way_vat_invoice'
#     _description = 'bright_way_vat_invoice.bright_way_vat_invoice'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
