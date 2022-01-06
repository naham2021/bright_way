# -*- coding: utf-8 -*-
# from odoo import http


# class BrightWayQrInvoice(http.Controller):
#     @http.route('/bright_way_qr_invoice/bright_way_qr_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bright_way_qr_invoice/bright_way_qr_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bright_way_qr_invoice.listing', {
#             'root': '/bright_way_qr_invoice/bright_way_qr_invoice',
#             'objects': http.request.env['bright_way_qr_invoice.bright_way_qr_invoice'].search([]),
#         })

#     @http.route('/bright_way_qr_invoice/bright_way_qr_invoice/objects/<model("bright_way_qr_invoice.bright_way_qr_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bright_way_qr_invoice.object', {
#             'object': obj
#         })
