# -*- coding: utf-8 -*-
# from odoo import http


# class BrightWayVatInvoice(http.Controller):
#     @http.route('/bright_way_vat_invoice/bright_way_vat_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bright_way_vat_invoice/bright_way_vat_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bright_way_vat_invoice.listing', {
#             'root': '/bright_way_vat_invoice/bright_way_vat_invoice',
#             'objects': http.request.env['bright_way_vat_invoice.bright_way_vat_invoice'].search([]),
#         })

#     @http.route('/bright_way_vat_invoice/bright_way_vat_invoice/objects/<model("bright_way_vat_invoice.bright_way_vat_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bright_way_vat_invoice.object', {
#             'object': obj
#         })
