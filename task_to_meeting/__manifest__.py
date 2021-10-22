# -*- coding: utf-8 -*-

{
    'name': "Task to Meeting",
    'summary': """
        Create meeting from task """,
    'description': """
        Create metting from task
    """,
    'license': 'OPL-1',
    'author': "Vivan Bhatt",
    'category': 'Event',
    'version': '12.0.1.0',
    'depends': ['project', 'calendar'],
    'data': [
        'wizard/metting_view.xml',
        'views/project_task.xml',
    ],
    'price': 9.00,
    'currency': 'EUR',
}