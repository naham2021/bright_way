# -*- coding: utf-8 -*-

import math

from odoo import http, _, fields,models
from odoo.http import request
from datetime import datetime, timedelta
from odoo.exceptions import UserError
# from odoo.addons.website_portal.controllers.main import website_account
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
from odoo.osv.expression import OR
# class website_account(website_account):
class CustomerPortal(CustomerPortal):

#     @http.route()
#     def account(self, **kw):
#         response = super(website_account, self).account(**kw)
#         partner = request.env.user
#         holidays = request.env['hr.leave']
#         holidays_count = holidays.sudo().search_count([
#         ('user_id', 'child_of', [request.env.user.id]),
#           ])
#         response.qcontext.update({
#         'holidays_count': holidays_count,
#         })
#         return response
    
    def _prepare_portal_layout_values(self):
        values = super(CustomerPortal, self)._prepare_portal_layout_values()
        partner = request.env.user
        holidays = request.env['hr.leave']
        holidays_count = holidays.sudo().search_count([
        ('user_id', 'child_of', [request.env.user.id]),
        # ('type','=','remove')
          ])
        print(">>>>>>>>>>>>>>>>H Count ",holidays_count)
        values.update({
        'holidays_count': holidays_count,
        })
        return values
    
    @http.route(['/my/leave_request', '/my/leave_request/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_leave_request(self, page=1, sortby=None, search=None, search_in='all',**kw):
        if not request.env.user.has_group('odoo_leave_request_portal_employee.group_employee_leave'):
            # return request.render("odoo_timesheet_portal_user_employee.not_allowed_leave_request")
            return request.render("odoo_leave_request_portal_employee.not_allowed_leave_request")
        response = super(CustomerPortal, self)
        values = self._prepare_portal_layout_values()
        holidays_obj = http.request.env['hr.leave']
        domain = [
            ('employee_id', '=', [request.env.user.employee_id.id,]),
            # ('type','=','remove')
        ]
        # count for pager
        holidays_count = http.request.env['hr.leave'].sudo().search_count(domain)
        # pager
        # pager = request.website.pager(
        pager = portal_pager(
            url="/my/leaves",
            total=holidays_count,
            page=page,
            step=self._items_per_page
        )
        sortings = {
            'date': {'label': _('Newest'), 'order': 'state,request_date_from desc'},
        }
        searchbar_sortings = {
            'date': {'label': _('Request Date'), 'order': 'request_date_from desc'},
            
             'state': {'label': _('Status'), 'order': 'state'},
        }
        searchbar_input = {
            'input': {'label': _('Request Date'), 'input': 'request_date_from'},
            
             'state': {'label': _('Status'), 'order': 'state'},
        }
        searchbar_inputs = {
            'name': {'input': 'name', 'label': _('Search in Description')},
            'holiday_status_id': {'input': 'holiday_status_id', 'label': _('Search in Holiday Type')},
            # 'state': {'input': 'state', 'label': _('Search in State')},
            'all': {'input': 'all', 'label': _('Search in All')},
        }
        # search
        domain_mng = []
        domain_ch=[]
        if search and search_in:
            search_domain = []
            # if search_in in ('state', 'all'):
            #     search_domain = OR([search_domain, [('state', 'ilike', search),]])
            if search_in in ('holiday_status_id', 'all'):
                search_domain = OR([search_domain, [('holiday_status_id', 'ilike', search),]])
            if search_in in ('name', 'all'):
                search_domain = OR([search_domain, [('name', 'ilike', search),]])
        
            domain += search_domain
            domain_ch += search_domain
            domain_mng += search_domain

        if not sortby:
            sortby = 'date'
        order = searchbar_sortings[sortby]['order']
        
        holidays = holidays_obj.sudo().search(domain, order=order, limit=self._items_per_page, offset=pager['offset'])
        domain_ch += [
            ('employee_id.coach_id.user_id', 'in', [request.env.user.id,]),
            
        ]
        
        holidays_coach = holidays_obj.sudo().search(domain_ch, order=order, limit=self._items_per_page, offset=pager['offset'])
        
        domain_mng += [
            ('employee_id.parent_id.user_id', 'in', [request.env.user.id,]),
            
        ]
        holidays_manager = holidays_obj.sudo().search(domain_mng, order=order, limit=self._items_per_page, offset=pager['offset'])
        
        
        values.update({
            'holidays': holidays,
            'page_name': 'holidays',
            'holidays_coach':holidays_coach,
            'holidays_manager':holidays_manager,
            'sortings' : sortings,
            'searchbar_sortings': searchbar_sortings,
            'searchbar_inputs':searchbar_inputs,
            'sortby': sortby,
            'search_in': search_in,
            'search': search,
            'pager': pager,
            'default_url': '/my/holidays',
        })
        return request.render("odoo_leave_request_portal_employee.display_leave_request", values)



class mailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    message_attachment_count = fields.Integer('Attachment Count', compute='_compute_message_attachment_count', groups="base.group_user,odoo_leave_request_portal_employee.group_employee_leave")
