# -*- coding: utf-8 -*-
{
    'name': "car_module",

    'summary': """
       Odoo exercise part 2""",

    'description': """
    Odoo exercise part 2. 
    Start date 03/01/2023
    End date before start Lunar New Year 2023""",

    'author': "Linh Thuy",
    'website': "",
    'category': 'Car Management',
    'version': '0.1',
    'depends': [
        'base',
        'report_xlsx',
        'hr',
    ],

    # always loaded
    'data': [
        # 'data/car_sequence.xml',
        'security/security_groups.xml',
        'security/security_rules.xml',
        'security/ir.model.access.csv',
        'report/car_report_views.xml',
        'wizard/cars_wizard_views.xml',
        'views/templates.xml',
        'views/car_car_views.xml',
        'views/parking_views.xml',
        'views/menus.xml',
        'views/hr_employee_views.xml',
    ],
}
