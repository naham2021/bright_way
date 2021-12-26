# -*- coding: utf-8 -*-
{
    'name': 'Centione Hr Loan',
    'version': '1.0',
    'category': '',
    'website': 'https://www.centione.com',
    'summary': '',
    'author':'Centione',
    'description': """
The module applies the following:
=================================
* Manange Loans for employees
* deducate loans in employees payslip
    """,
    'depends': [
        'hr',
        'centione_hr_payroll_base',
        'account',
    ],
    'data': [
        'data/hr_loan_data.xml',
        'data/acc_payment_loan.xml',
        'wizard/loan_payment_wizard.xml',
        'wizard/loan_register_payment_wizard.xml',
        'wizard/loan_account_payment_wizard.xml',
        'wizard/paymentdelay_wizard.xml',
        'views/loan_view.xml',
        'views/hr_employee.xml',
        'views/hr_contract.xml',
        'views/account_journal_inherit_view.xml',
        'views/acc_loan_payment_view.xml',
        'views/account_payment_inherit_view.xml',
        'security/ir.model.access.csv',
    ],
    'application': True
}
