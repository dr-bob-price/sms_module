# -*- coding: utf-8 -*-
from odoo import models
from odoo import fields
from odoo import api

class sms(models.Model):
    _inherit = 'purchase.order'
    sms_project_code = fields.Many2one('sms.menue', 'SMS Project Code')
    sms_project = fields.Char(string='SMS Project', related='sms_project_code.descrip', readonly='True')
    sms_po_requestor = fields.Many2one('res.partner', 'Requestor')
    sms_sage_code = fields.Many2one('sms.menuf', 'SMS Sage Code')
    sms_po_received = fields.Boolean('Order Placed', help="Has supplier acknowledged PO?")
    sms_proforma_supp = fields.Char('Supplier Name', help="Supplier for Pro-Forma POs", default="Not Needed for Standard POs")
    sms_contact_account = fields.Char(string='ContactRef: SMS', related='partner_id.sms_contact_accountno', readonly='True')
    partner_ref = fields.Char(related='partner_id.sms_contact_accountno', readonly='True')
    sms_po_notes = fields.Text('Notes on PO', help="Notes to appear on PO")


