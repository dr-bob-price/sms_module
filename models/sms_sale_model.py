# -*- coding: utf-8 -*-
from odoo import models
from odoo import fields
from odoo import api

class sms(models.Model):
    _inherit = 'sale.order'
    sms_agent = fields.Many2one('res.partner', 'SMS Agent')
    sms_shipto = fields.Many2one('res.partner', 'Ship To')
    sms_invoiceto = fields.Many2one('res.partner', 'Invoice To')
    sms_job_number = fields.Char('SMS Job Number:', help="Enter SMS Job Number")
    sms_so_notes = fields.Text(string='Notes on SO', help="Enter Notes to Appear on the Sales Order")
    
