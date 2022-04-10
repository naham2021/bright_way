{
    'name': 'Show Last Order Line',
    'summary': 'Show the last price, last quantity of product were supplied to customer before.',
    'description': 'Show the last price, last quantity of product were supplied to customer before.',
    'author': "Sonny Huynh",
    'category': 'Sales',
    'version': '0.1',
    'depends': ['sale'],

    # always loaded
    'data': [
        'views/form_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'images': [
        'static/description/banner.png',
    ],
    'license': 'LGPL-3',
}