# -*- coding: utf-8 -*-
{
    'name': "nakham_security_groups",

    'summary': """
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Centione",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','nakham_customer_area_sequence','account','account_reports','product','account_asset'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
