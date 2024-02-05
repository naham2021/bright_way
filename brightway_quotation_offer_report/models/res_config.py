from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    english_sale_terms = fields.Text(string="English Terms & Conditions", readonly=False)
    ar_invoice_terms = fields.Text(string="English Terms & Conditions", readonly=False)



class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    english_sale_terms = fields.Text(string='English Terms & Conditions', related='company_id.english_sale_terms', readonly=False)
    ar_invoice_terms = fields.Text(string="English Terms & Conditions", related='company_id.ar_invoice_terms', readonly=False)


    english_use_sale_terms = fields.Boolean(
        string='Default English Terms & Conditions',
        config_parameter='sale.english_use_sale_terms')

    ar_use_sale_terms = fields.Boolean(
        string='Default Terms & Conditions',
        config_parameter='sale.ar_use_sale_terms')

