# -*- coding: utf-8 -*-
from odoo import models
from odoo import fields
from odoo import api

class sms(models.Model):
    _inherit = 'maintenance.equipment'
    sms_equip_carrier = fields.Many2one('stock.picking', 'Stock Transfer')
    sms_equip_sales_order = fields.Many2one('sale.order', 'Sales Order')
    sms_equip_purchase_order = fields.Many2one('purchase.order', 'Purchase Order') 
    sms_equip_manufacture_order = fields.Many2one('mrp.production', 'Manufacturing Order')
    sms_equip_manufacture_orderb = fields.Many2one('mrp.production', 'Sub M/O 1')
    sms_equip_manufacture_orderc = fields.Many2one('mrp.production', 'Sub M/O 2')
    sms_equip_manufacture_orderd = fields.Many2one('mrp.production', 'Sub M/O 3')
    sms_equip_manufacture_ordere = fields.Many2one('mrp.production', 'Sub M/O 4')
    sms_equip_manufacture_orderf = fields.Many2one('mrp.production', 'Sub M/O 5')
    sms_equip_manufacture_orderg = fields.Many2one('mrp.production', 'Sub M/O 6')
    sms_equip_manufacture_orderh = fields.Many2one('mrp.production', 'Sub M/O 7')

    sms_equip_optiona = fields.Many2one('product.template', 'Accessory 1')
    sms_equip_optionb = fields.Many2one('product.template', 'Accessory 2')


    sms_equip_move_raw_ids = fields.One2many(string='Manufacturing', related='sms_equip_manufacture_order.move_raw_ids', readonly='True')   
    sms_equip_customer_country = fields.Many2one(string='Country', related='sms_equip_sales_order.partner_id.country_id', readonly='True', store=True)
    sms_equip_customer_state = fields.Many2one(string='State/Region', related='sms_equip_sales_order.partner_id.state_id', readonly='True', store=True)
    sms_equip_customer = fields.Many2one(string='Customer', related='sms_equip_sales_order.partner_id', readonly='True', store=True)


    sms_cproduct_code = fields.Many2one(string='SMS Product', related='sms_equip_sales_order.product_id', readonly='True', store=True)


    sms_equip_supplier = fields.Many2one(string='Vendor', related='sms_equip_purchase_order.partner_id', readonly='True')
    sms_sproduct_code = fields.Many2one(string='Product', related='sms_equip_purchase_order.product_id', readonly='True')
    sms_carrier = fields.Many2one(string='Carrier Name', related='sms_equip_carrier.carrier_id', readonly='True')
    sms_carrier_track = fields.Char(string='Carrier Track Ref', related='sms_equip_carrier.carrier_tracking_ref', readonly='True')
    sms_customs_export = fields.Char('Customs Nos (Exp)', help="Enter Customs Export Number")
    sms_customs_import = fields.Char('Customs Nos (Imp)', help="Enter Customs Import Number")
    sms_install_date = fields.Date('Install Date', help="Enter Date System was Installed")
    sms_training_date = fields.Date('Training Date', help="Enter Date Training was Started")
    sms_installer = fields.Many2one('res.partner', help="Enter person who installed equipment")
    sms_trainer = fields.Many2one('res.partner', help="Enter person who carried out the training")

#legacy fields for ACT import
    sms_legacy_customer = fields.Many2one('res.partner', 'Customer (old)')
    sms_legacy_dvsoptions = fields.Char('DVS Options', help="Legacy Data")
    sms_legacy_balancetype = fields.Many2one('sms.menu', 'Balance Type (old)')
    sms_balancetype = fields.Many2one('product.product', 'Balance Type')
    sms_legacy_balanceheadsn = fields.Char('Balance Head S/N', help="Legacy Data")
    sms_legacy_balanceboardsn = fields.Char('Balance Board S/N', help="Legacy Data")
    sms_legacy_mfctype = fields.Many2one('product.product', 'DVS MFC Type')
    sms_legacy_mfcsize = fields.Char('MFC Size', help="Legacy Data")
    sms_legacy_probetype = fields.Many2one('product.product', 'Probe Type')
    sms_legacy_hdwirelen = fields.Char('HD Wire Length', help="Legacy Data")
    sms_legacy_dpaheadsn = fields.Char('DPA Head S/N', help="Legacy Data")
    sms_legacy_dpaelecsn = fields.Char('DPA Electronics S/N', help="Legacy Data")
    sms_legacy_eurothermsn = fields.Char('Eurotherm S/N', help="Legacy Data")
    sms_legacy_cameratype = fields.Char('Camera Type', help="Legacy Data")
    sms_legacy_accsports = fields.Boolean('DVS Accessory Ports', help="Legacy Data")
    sms_legacy_preheattype = fields.Many2one('product.product', 'Pre-Heat Type')
    sms_legacy_valvetype = fields.Many2one('sms.menu', 'Valve Type')
    sms_legacy_ovmtype = fields.Many2one('sms.menu', 'OVM Type')
    sms_legacy_incubatortype = fields.Many2one('sms.menu', 'Incubator Type (old)')
    sms_incubatortype = fields.Many2one('product.product', 'Incubator Type')
    sms_legacy_bottlesize = fields.Char('Bottle Size', help="Legacy Data")
    sms_legacy_bottleqty = fields.Char('Bottle Qty', help="Legacy Data")
    sms_legacy_computerspec = fields.Char('Computer Spec', help="Legacy Data")
    sms_legacy_computeros = fields.Many2one('sms.menud', 'Operating System')
    sms_legacy_computersn = fields.Char('Computer S/N', help="Legacy Data")

    sms_legacy_dataacq = fields.Many2one('sms.menud', 'Data Aquisition Card')
    sms_legacy_username = fields.Char('Username', help="Legacy Data")
    sms_legacy_password = fields.Char('Password', help="Legacy Data")
    sms_legacy_ctrlsoftware = fields.Many2one('product.product', 'Control Software')
    sms_legacy_analysissoftware = fields.Char('Analysis Software', help="Legacy Data")

    sms_legacy_gassupplya = fields.Many2one('sms.menub', 'Gas Supply 1')
    sms_legacy_gassupplyb = fields.Many2one('sms.menub', 'Gas Supply 2')
    sms_legacy_gassupplyc = fields.Many2one('sms.menub', 'Gas Supply 3')
    sms_legacy_gassupplyd = fields.Many2one('sms.menub', 'Gas Supply 4')
    sms_legacy_gassupplye = fields.Many2one('sms.menub', 'Gas Supply 5')

    sms_legacy_upsa = fields.Char('UPS System 1', help="Legacy Data")
    sms_legacy_upsb = fields.Char('UPS System 2', help="Legacy Data")
    sms_legacy_voltage = fields.Char('Voltage', help="Legacy Data")
    sms_legacy_table = fields.Many2one('sms.menuc', 'Table Type')


    sms_legacy_seractive = fields.Boolean('Service Contract Active', help="Legacy Data")
    sms_legacy_sertype = fields.Many2one('sms.menuc', 'Paid/Full/MO/Warranty')
    sms_legacy_serstartdate = fields.Date('Service Start Date', help="Enter Date")
    sms_legacy_serenddate = fields.Date('Service End Date', help="Enter Date")









