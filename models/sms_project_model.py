# -*- coding: utf-8 -*-
from odoo import models
from odoo import fields
from odoo import api

class sms(models.Model):
    _inherit = 'project.task'
    eco_source_part = fields.Many2one('product.product', 'Archived Part')
    eco_create_part = fields.Many2one('product.product', 'Part')     
    sms_customer = fields.Many2one('res.partner', 'Customer')
