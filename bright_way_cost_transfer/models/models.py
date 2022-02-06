from odoo import models, fields, api,_


class bright_way_cost_transfer(models.Model):
    _inherit = 'stock.move'

    cost = fields.Float('cost',compute='_calc_cost',store=True)

    @api.depends('product_id.standard_price','quantity_done')
    def _calc_cost(self):
        for r in self:
            r.cost = r.product_id.standard_price * r.quantity_done
class bright_way_cost_transfer(models.Model):
    _inherit = 'stock.move.line'

    cost = fields.Float('cost',compute='_calc_cost',store=True)


    @api.depends('product_id.standard_price','qty_done')
    def _calc_cost(self):
        for r in self:
            r.cost = r.product_id.standard_price * r.qty_done
class bright_way_cost_transfer(models.Model):
    _inherit = 'stock.picking'

    op_type = fields.Selection(related='picking_type_id.code',store=True)
