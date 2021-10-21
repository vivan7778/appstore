# -*- coding: utf-8 -*-

from odoo import models, fields


class CalendarEvents(models.Model):
    _inherit = 'calendar.event'

    task_id = fields.Many2one('project.task')



    def view_task(self):
        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'calendar.event',
            'target': 'current',
            'res_id': self.task_id.id,
            'type': 'ir.actions.act_window'
        }

