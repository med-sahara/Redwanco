# -*- coding: utf-8 -*-
{
        'name': 'Sales Order Type OU',
        'version': '12.0.1.0.10',
        'summary': 'Operational unit in sale order type',
        'category': 'Sale',
        'author': 'Cybrosys Techno Solutions',
        'maintainer': 'Cybrosys Techno Solutions',
        'company': 'Cybrosys Techno Solutions',
        'website': 'https://www.cybrosys.com',
        'depends': ['base', 'sale', 'sale_order_type'],
        'data': [
                'views/sale_order_ou.xml'
        ],
        'images': ['static/description/icon.png'],
        'license': 'AGPL-3',
        'installable': True,
        'application': False,
        'auto_install': False,
}
