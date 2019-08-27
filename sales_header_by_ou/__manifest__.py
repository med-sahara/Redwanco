# -*- coding: utf-8 -*-
{
        'name': 'Sales Header By OU',
        'version': '12.0.1.0.10',
        'summary': 'Sales Header By OU',
        'category': 'Sale',
        'author': 'Vinaya S B',
        'maintainer': 'Cybrosys Techno Solutions',
        'company': 'Cybrosys Techno Solutions',
        'website': 'https://www.cybrosys.com',
        'depends': ['base', 'sale','sale_management','operating_unit'],
        'data': [
                'views/sale_header.xml'
        ],
        'images': ['static/description/icon.png'],
        'license': 'AGPL-3',
        'installable': True,
        'application': False,
        'auto_install': False,
}
