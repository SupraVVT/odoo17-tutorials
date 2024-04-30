# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Estate',
    'version': '1.0',
    'summary': 'Estate tutorial',
    'description': "Odoo 17 Tutorial - Estate",
    'sequence': -1,
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/estate_demo_data.xml',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],

    'application': True,
}