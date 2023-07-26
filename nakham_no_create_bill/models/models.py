from odoo import api, models, fields,_
from odoo.osv import osv
import odoo.addons.decimal_precision as dp
from odoo.exceptions import UserError, ValidationError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def action_view_invoice(self):

        '''
        This function returns an action that display existing vendor bills of given purchase order ids.
        When only one found, show the vendor bill immediately.
        '''
        action = self.env.ref('account.action_move_in_invoice_type')
        result = action.read()[0]
        create_bill = self.env.context.get('create_bill', False)
        print("create_bill :: ",create_bill)
        # override the context to get rid of the default filtering
        if create_bill == True:
            flag = 0
            for line in self.order_line:
                print("line product ", line.product_id.name)
                if line.qty_invoiced != 0:
                    if line.qty_received - line.qty_invoiced == 0:
                        flag = 1
                        break
                    elif line.qty_received - line.qty_invoiced != 0:
                        flag = 0
                else:
                    flag = 0
            if flag == 1:
                raise ValidationError(_("You cannot Create Bill IF Qty Received Equal Qty Billed."))
        result['context'] = {
            'default_type': 'in_invoice',
            'default_company_id': self.company_id.id,
            'default_purchase_id': self.id,
        }
        # choose the view_mode accordingly
        if len(self.invoice_ids) > 1 and not create_bill:
            result['domain'] = "[('id', 'in', " + str(self.invoice_ids.ids) + ")]"
        else:
            res = self.env.ref('account.view_move_form', False)
            form_view = [(res and res.id or False, 'form')]
            if 'views' in result:
                result['views'] = form_view + [(state, view) for state, view in action['views'] if view != 'form']
            else:
                result['views'] = form_view
            # Do not set an invoice_id if we want to create a new bill.
            if not create_bill:
                result['res_id'] = self.invoice_ids.id or False
        result['context']['default_origin'] = self.name
        result['context']['default_reference'] = self.partner_ref
        print("result :: ",result)
        return result


    # def action_view_invoice_new(self):
    #     print("enter hererer ")
    #     '''
    #     This function returns an action that display existing vendor bills of given purchase order ids.
    #     When only one found, show the vendor bill immediately.
    #     '''
    #     action = self.env.ref('account.action_move_in_invoice_type')
    #     result = action.read()[0]
    #     create_bill = self.env.context.get('create_bill', False)
    #     # override the context to get rid of the default filtering
    #     result['context'] = {
    #         'default_type': 'in_invoice',
    #         'default_company_id': self.company_id.id,
    #         'default_purchase_id': self.id,
    #         'default_partner_id': self.partner_id.id,
    #     }
    #     # Invoice_ids may be filtered depending on the user. To ensure we get all
    #     # invoices related to the purchase order, we read them in sudo to fill the
    #     # cache.
    #     self.sudo()._read(['invoice_ids'])
    #     # choose the view_mode accordingly
    #     if len(self.invoice_ids) > 1 and not create_bill:
    #         result['domain'] = "[('id', 'in', " + str(self.invoice_ids.ids) + ")]"
    #     else:
    #         res = self.env.ref('account.view_move_form', False)
    #         form_view = [(res and res.id or False, 'form')]
    #         if 'views' in result:
    #             result['views'] = form_view + [(state,view) for state,view in action['views'] if view != 'form']
    #         else:
    #             result['views'] = form_view
    #         # Do not set an invoice_id if we want to create a new bill.
    #         if not create_bill:
    #             result['res_id'] = self.invoice_ids.id or False
    #     result['context']['default_invoice_origin'] = self.name
    #     result['context']['default_ref'] = self.partner_ref
    #     return result
