# -*- coding: utf-8 -*-
{
        'name': 'Sales Order Type ST',
        'version': '12.0.1.0.0',
        'summary': 'Sales Team in sale order type',
        'category': 'Sale',
        'author': '',
        'depends': ['base', 'sale', 'sale_order_type','sales_team'],
        'data': [
                'views/sale_order_st.xml'
        ],
        'installable': True,
        'application': False,
        'auto_install': False,
}
