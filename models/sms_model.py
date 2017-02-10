# -*- coding: utf-8 -*-
from odoo import models
from odoo import fields
from odoo import api

class sms(models.Model):
    _name = 'sms.menu'
    name = fields.Char('Name', required=True)
    descrip = fields.Char('Description', required=False)
#    sms_equip_carrier = fields.Many2one('stock.picking', 'Stock Transfer')
#    sms_equip_sales_order = fields.Many2one('sale.order', 'Sales Order')
#    sms_equip_purchase_order = fields.Many2one('purchase.order', 'Purchase Order')     
#    sms_equip_customer_country = fields.Many2one(string='Country', related='sms_equip_sales_order.partner_id.country_id', readonly='True')
#    sms_equip_customer = fields.Many2one(string='Customer', related='sms_equip_sales_order.partner_id', readonly='True')
#    sms_cproduct_code = fields.Many2one(string='Product', related='sms_equip_sales_order.product_id', readonly='True')
#    sms_carrier = fields.Many2one(string='Carrier', related='sms_equip_sales_order.carrier_id', readonly='True')
#    sms_equip_supplier = fields.Many2one(string='Vendor', related='sms_equip_purchase_order.partner_id', readonly='True')
#    sms_sproduct_code = fields.Many2one(string='Product', related='sms_equip_purchase_order.product_id', readonly='True')
#    sms_carrier = fields.Many2one(string='Carrier Name', related='sms_equip_carrier.carrier_id', readonly='True')
#    sms_carrier_track = fields.Char(string='Carrier Track Ref', related='sms_equip_carrier.carrier_tracking_ref', readonly='True')
#    sms_customs_export = fields.Char('Customs Nos (Exp)', help="Enter Customs Export Number")
#    sms_customs_import = fields.Char('Customs Nos (Imp)', help="Enter Customs Import Number")


 
