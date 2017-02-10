# -*- coding: utf-8 -*-
from odoo import models
from odoo import fields
from odoo import api

class sms(models.Model):
    _name = 'sms.menue'
    name = fields.Char('Name', required=True)
    descrip = fields.Char('Description', required=False)



 
