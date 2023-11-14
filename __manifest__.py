# -*- coding: utf-8 -*-
{
    'name': "Vietcaphe",

    'summary': """
        Ajouter champ Seuil dans produits. Afficher les produits qui ont le stock inferieur à seuil dans Inventaire/Analyse/Alerte Stock Minimum""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Index Consulting Madagascar",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'stock'],

    # always loaded
    'data': [
        'views/product_template.xml', 
        'views/stock.xml',
    ],
}