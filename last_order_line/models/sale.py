from odoo import api, models, fields


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    last_purchase = fields.Html(string='Last Purchase', compute='_compute_last_purchase', store=False, copy=False)

    @api.depends('product_id', 'order_id.partner_id')
    def _compute_last_purchase(self):
        for line in self:
            if line.product_id.id and line.order_partner_id.id and line.order_id.state not in ['sale', 'done']:

                last_sale_line = self.env['sale.order.line'].search([('product_id', '=', line.product_id.id),
                                                                     (
                                                                     'order_partner_id', '=', line.order_partner_id.id),
                                                                     ('is_delivery', '=', False),
                                                                     ('state', 'in', ['sale', 'done'])], limit=1)

                if line.order_id.ids:
                    last_quote_line = self.env['sale.order.line'].search([('product_id', '=', line.product_id.id),
                                                                          ('order_partner_id', '=',
                                                                           line.order_partner_id.id),
                                                                          ('is_delivery', '=', False),
                                                                          ('state', 'in', ['draft', 'sent']),
                                                                          ('order_id', '<', line.order_id.ids[0])], limit=1)
                else:
                    last_quote_line = self.env['sale.order.line'].search([('product_id', '=', line.product_id.id),
                                                                          ('order_partner_id', '=',
                                                                           line.order_partner_id.id),
                                                                          ('is_delivery', '=', False),
                                                                          ('state', 'in', ['draft', 'sent'])], limit=1)

                last_so_line = False

                Order_info = ''
                if last_sale_line or (last_sale_line and line.order_id.ids and line.order_id.ids[0] != last_sale_line.order_id.id):
                    last_so_line = last_sale_line
                    Order_info = "Order: " + str(last_so_line.order_id.name)
                elif last_quote_line or (last_quote_line and line.order_id.ids and line.order_id.ids[0] != last_quote_line.order_id.id):
                    last_so_line = last_quote_line
                    Order_info = "Quote: " + str(last_quote_line.order_id.name)

                if last_so_line:
                    line.last_purchase = "Qty: " + str(last_so_line.product_uom_qty) + "<br/>" \
                                         + "Unit Price: " + str(last_so_line.price_unit) + "<br/>" \
                                         + "Discount: " + str(last_so_line.discount) + "%<br/>" + \
                                         "Price (Tax Excl): " + str(last_so_line.price_reduce) + "<br/>" + \
                                         Order_info \
                                         + " (" + str(last_so_line.order_id.date_order.strftime('%d/%m/%Y')) + ")"
                else:
                    line.last_purchase = ""
            else:
                line.last_purchase = ""
