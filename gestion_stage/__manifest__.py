# -*- coding: utf-8 -*-
{
    'name': "gestion_stage",

    'summary': "Module de gestion des demandes et conventions de stage",

    'description': """
        Module pour gérer les demandes de stage et les conventions de stage à l\'ENSA.
    """,

    'author': "najat salhi",
    'website': "http://ensao.ump.ma/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/etudiant_views.xml',
        'views/demande_stage_views.xml',
        'views/convention_stage_views.xml',
        'views/menu.xml',
        'views/demande_stage_report.xml',
        'views/demande_stage_report_action.xml'  # Ensure this line is included
    ],
     'images': ['static/description/icon.png'], 
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

