# -*- coding: utf-8 -*-
{
    'name': "mps",

    'summary': """
        Theme for mps system,
        """,

    'description': """
        Theme for mps HP
    """,

    'author': "Planes Soluciones Informáticas",
    'website': "https://www.planesnet.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Theme/Creative',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

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