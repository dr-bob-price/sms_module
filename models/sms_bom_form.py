# -*- coding: utf-8 -*-
from odoo import models
from odoo import fields
from odoo import api

class sms(models.Model):
    _inherit = 'mrp.bom'
    sms_bom_cost = fields.Float(string='BOM Cost', readonly='True')


  
    @api.multi
    def write(self, vals):
        line_cost = 0
        total = 0
        for n in self.bom_line_ids.ids:
            line_product_id = self.bom_line_ids.browse(n).product_id.ids
            line_product_cost = self.bom_line_ids.browse(n).product_id.browse(line_product_id).sms_cost
            line_cost = self.bom_line_ids.browse(n).product_qty * line_product_cost
            total = total + line_cost
        vals['sms_bom_cost']=total 
        super(sms, self).write(vals)
        return True
