# -*- coding: utf-8 -*-
# from odoo import http


# class BrightWayJournalFields(http.Controller):
#     @http.route('/bright_way_journal_fields/bright_way_journal_fields/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bright_way_journal_fields/bright_way_journal_fields/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bright_way_journal_fields.listing', {
#             'root': '/bright_way_journal_fields/bright_way_journal_fields',
#             'objects': http.request.env['bright_way_journal_fields.bright_way_journal_fields'].search([]),
#         })

#     @http.route('/bright_way_journal_fields/bright_way_journal_fields/objects/<model("bright_way_journal_fields.bright_way_journal_fields"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bright_way_journal_fields.object', {
#             'object': obj
#         })
