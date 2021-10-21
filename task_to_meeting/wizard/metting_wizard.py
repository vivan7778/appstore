# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError

class CreateMeeting(models.TransientModel):
    _name = 'create.meeting'
    _description = 'set meeting date'

    start_date = fields.Datetime(string="Start Date")
    end_date = fields.Datetime(string="End Date")

    def action_create_metting(self):
        project = self.env['project.task'].browse(self._context.get(
            'active_id'))
        if project.partner_id:
            self.env['calendar.event'].create({
                'name': project.name,
                'partner_ids': [(4, project.partner_id.id)],
                'user_id':project.user_id.id,
                'start':self.start_date,
                'stop':self.end_date,
                'task_id' : project.id
                })
        else:
            raise UserError(_('Please select Partner'))
