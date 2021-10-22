# -*- coding: utf-8 -*-

from odoo import models, fields,_


class ProjectTask(models.Model):
    _inherit = "project.task"

    calendar_ids = fields.One2many('calendar.event','task_id')
    check_meeting = fields.Boolean('Check Meeting', compute='_compute_check_meeting')

    def _compute_check_meeting(self):
        if self.calendar_ids:
            self.check_meeting = True
        else:
            self.check_meeting = False



    def preview_meeting(self):
        return {
                'name': _('Meeting Detail'),
                'type': 'ir.actions.act_window',
                'res_model': 'calendar.event',
                'view_type':'form',
                'view_mode': 'tree,form',
                'view_id': False,
                'res_id': False,
                'domain': [('id', 'in', self.mapped('calendar_ids').ids)],
                'target':'current'
    }