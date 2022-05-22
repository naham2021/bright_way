# -*- coding: utf-8 -*-
# from odoo import http


# class BrightWayPickingOperationsEdit(http.Controller):
#     @http.route('/bright_way_picking_operations_edit/bright_way_picking_operations_edit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bright_way_picking_operations_edit/bright_way_picking_operations_edit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bright_way_picking_operations_edit.listing', {
#             'root': '/bright_way_picking_operations_edit/bright_way_picking_operations_edit',
#             'objects': http.request.env['bright_way_picking_operations_edit.bright_way_picking_operations_edit'].search([]),
#         })

#     @http.route('/bright_way_picking_operations_edit/bright_way_picking_operations_edit/objects/<model("bright_way_picking_operations_edit.bright_way_picking_operations_edit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bright_way_picking_operations_edit.object', {
#             'object': obj
#         })
