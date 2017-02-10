# -*- coding: utf-8 -*-
from odoo import models
from odoo import fields
from odoo import api

class sms(models.Model):
    _inherit = 'mrp.bom.line'

    sms_location = fields.Text(string='StockLoc', related='product_id.product_tmpl_id.description_picking', readonly='True', store=True)
    sms_bom_location = fields.Text(string='StockLoc', related='product_id.product_tmpl_id.description_picking', readonly='True', store=True)
    sms_cost_bom = fields.Float(string='Cost', related='product_id.product_tmpl_id.sms_cost', readonly='True', store=True)


