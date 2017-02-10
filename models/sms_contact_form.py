# -*- coding: utf-8 -*-
from odoo import models
from odoo import fields
from odoo import api

class sms(models.Model):
    _inherit = 'res.partner'
    sms_product = fields.Many2one('product.product', 'Event/Product 1')
    sms_productb = fields.Many2one('product.product', 'Event/Product 2')
    sms_productc = fields.Many2one('product.product', 'Event/Product 3')
    sms_productd = fields.Many2one('product.product', 'Event/Product 4')
    sms_producte = fields.Many2one('product.product', 'Event/Product 5')
    sms_productf = fields.Many2one('product.product', 'Event/Product 6')
    sms_productg = fields.Many2one('product.product', 'Event/Product 7')
    sms_producth = fields.Many2one('product.product', 'Event/Product 8')
    sms_producti = fields.Many2one('product.product', 'Event/Product 9')
    sms_productj = fields.Many2one('product.product', 'Event/Product 10')
    sms_systema = fields.Many2one('maintenance.equipment', 'Installed System 1')
    sms_systemb = fields.Many2one('maintenance.equipment', 'Installed System 2')
    sms_systemc = fields.Many2one('maintenance.equipment', 'Installed System 3')
    sms_systemd = fields.Many2one('maintenance.equipment', 'Installed System 4')
    sms_systeme = fields.Many2one('maintenance.equipment', 'Installed System 5')

    sms_contact_accountno = fields.Char('ContactsRef: SMS', help="Enter the reference number this contact uses to refer to SMS")
    sms_gm_accountno = fields.Char('GoldMine Account', help="GoldMine Account Number 1")
    sms_gm_uactid = fields.Char('ACT ID', help="ACT Database Unique ID")
    sms_gm_ucompuser = fields.Char('User name Comp. Product', help="Username")
    sms_gm_ualtemail = fields.Char('Alternate E-Mail', help="Alternative e-mail address")
    sms_gm_unda = fields.Boolean('NDA in place?', help="Non-disclosure agreement with contact?")
