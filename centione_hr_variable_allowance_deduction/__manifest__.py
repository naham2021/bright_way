# -*- coding: utf-8 -*-
{
    'name': "Centione Hr Variable Allowance & Deduction",

    'summary': """
        """,

    'description': """
    """,

    'author': "Centione",
    'website': "http://www.centione.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['centione_hr_contract', 'centione_hr_payroll_base'],

    # always loaded
    'data': [
        'views/hr_variable_allowance_deduction.xml',
        'views/hr_variable_allowance_deduction_type.xml',
        'security/ir.model.access.csv',
    ],
}