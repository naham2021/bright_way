from odoo import api, fields, models



class ResPartner(models.Model):
    _inherit = 'res.partner'

    iban_no = fields.Char(
        string='IBAN NO',
        required=False)

    supplying_duration = fields.Char(
        string='Supplying Duration',
        required=False)



class ResUsers(models.Model):
    _inherit = 'res.users'

    job_id = fields.Many2one(comodel_name="hr.job", string="Job Position")


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    terms_ar = fields.Text(
        string="الشروط و المعايير",
        required=False, related='company_id.ar_invoice_terms', )
    terms_en = fields.Text('Terms and conditions', related='company_id.english_sale_terms', )

    warranty = fields.Char(
        string='Warranty', 
        required=False)

    payment_id = fields.Many2one('account.payment', string="Payment")

    bank_account = fields.Char(
        string='Bank Account',
        required=False)