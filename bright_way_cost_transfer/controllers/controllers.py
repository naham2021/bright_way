# -*- coding: utf-8 -*-
# from odoo import http


# class BrightWayCostTransfer(http.Controller):
#     @http.route('/bright_way_cost_transfer/bright_way_cost_transfer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bright_way_cost_transfer/bright_way_cost_transfer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bright_way_cost_transfer.listing', {
#             'root': '/bright_way_cost_transfer/bright_way_cost_transfer',
#             'objects': http.request.env['bright_way_cost_transfer.bright_way_cost_transfer'].search([]),
#         })

#     @http.route('/bright_way_cost_transfer/bright_way_cost_transfer/objects/<model("bright_way_cost_transfer.bright_way_cost_transfer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bright_way_cost_transfer.object', {
#             'object': obj
#         })
