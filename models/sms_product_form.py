# -*- coding: utf-8 -*-
from odoo import models
from odoo import fields
from odoo import api

class sms(models.Model):
    _inherit = 'product.template'

    sms_part_number = fields.Char('SMS Part Number', help="SMS Part Number", readonly='True')
    sms_supplier = fields.Char('SMS Not Used', help="Supplier-OLD", readonly='True')
    sms_supplierb = fields.Many2one('res.partner', string="SMS Supplier", help="Supplier", readonly='True')
    sms_whereused_a = fields.Many2one('mrp.bom', 'Where Used a', readonly='True')
    sms_whereused_b = fields.Many2one('mrp.bom', 'Where Used b', readonly='True')
    sms_whereused_c = fields.Many2one('mrp.bom', 'Where Used c', readonly='True')
    sms_whereused_d = fields.Many2one('mrp.bom', 'Where Used d', readonly='True')
    sms_whereused_a_qty = fields.Integer(string='Where Used a qty', readonly='True')
    sms_whereused_b_qty = fields.Integer(string='Where Used b qty', readonly='True')
    sms_whereused_c_qty = fields.Integer(string='Where Used c qty', readonly='True')
    sms_whereused_d_qty = fields.Integer(string='Where Used d qty', readonly='True')
    sms_related_part = fields.Many2one('product.template', 'Related Part')


    sms_cost = fields.Float(string='SMS Cost', readonly='True')
    sms_cost_old = fields.Float(string='SMS Cost', readonly='True')
    sms_test = fields.Text(string='SMS Test', readonly='True')
    sms_testb = fields.Text(string='SMS Test', readonly='True')
    sms_qty_stock = fields.Float(string='Qty Stock', related='qty_available', readonly='True')
    sms_stock_value = fields.Float(string='SMS Stock Value', readonly='True')



    @api.model
    def create(self, vals):
        vals['sms_part_number'] = self.env['ir.sequence'].next_by_code('product.product') or '/'
        vals['default_code'] = vals['sms_part_number']
        return super(sms, self).create(vals)

    @api.multi
    def write(self, vals):
#   set seller to one with lowest price, cost to highest using unit of measures (uom) and exchange rates
#
#       set the sms_cost to whatever is in the product price field
        vals['sms_cost']= self.standard_price
#       work out unit of measure for this product
#       purchase UOM
        uom_p_id = self.uom_po_id.ids
        uom_p_factor = self.uom_po_id.browse(uom_p_id).factor_inv
#       sell/stock UOM
        uom_s_id = self.uom_id.ids
        uom_s_factor = self.uom_id.browse(uom_s_id).factor_inv
#       record product category
        prod_cat_id = self.categ_id.ids
        product_cat = self.categ_id.browse(prod_cat_id).name

#       set loop number/price to 0 so on first loop seller name is recorded and sms_cost set. If no suppliers sms_cost = standard_price
        start=0

#       loop through sellers, set supplier to one top of the list on first loop (start=0, should be cheapest)
        for n in self.seller_ids.ids:

            sellerid = self.seller_ids.browse(n).name.ids
            ex_rate_id = self.seller_ids.browse(n).currency_id.ids
            exchange_rate = self.seller_ids.browse(n).currency_id.browse(ex_rate_id).rate
            
            if start == 0:
                start = ((self.seller_ids.browse(n).price/uom_p_factor)/exchange_rate)*uom_s_factor
                vals['sms_supplier'] = self.seller_ids.browse(n).name.browse(sellerid).name
                loop=0
                for m in sellerid:
                    loop+=1
                    if loop == 1:
                        vals['sms_supplierb']=m
                vals['sms_cost'] = start
#           find highest price, set that to sms_cost using uom and exchange rate for that seller
            price = ((self.seller_ids.browse(n).price/uom_p_factor)/exchange_rate)*uom_s_factor
            if price > start:
                vals['sms_cost'] = price
                start = price

#       find bom and read out cost
        bom_ids = self.env['mrp.bom'].search([]).ids
        for record in bom_ids:
            bom_name = self.env['mrp.bom'].browse(record).product_tmpl_id.name
            if bom_name == self.name:
                vals['sms_cost'] = self.env['mrp.bom'].browse(record).sms_bom_cost

# if suppliers exist with a cost over 0 then update the price (always the case!), otherwise sms_cost = standard_price
        if vals['sms_cost'] > 0:
            vals['standard_price'] = vals['sms_cost']          
#        
#       calculate stock value
        vals['sms_stock_value']= self.qty_available * vals['sms_cost']

#       55% margin for products in All category *2.22
#       65% margin for products in Consumables category *2.86
#       70% margin for products in - category *3.33
#       75% margin for products in Accessories category *4
#       80% margin for products in Systems category *5

        sms_factor = 2.22
        if product_cat == 'Accessories':
            sms_factor = 3.33
        if product_cat == 'Consumables':
            sms_factor = 2.86
        if product_cat == 'Systems':
            sms_factor = 4
        if product_cat == 'Service':
            sms_factor = 1

#       update list price
        vals['list_price'] = vals['sms_cost'] * sms_factor
        super(sms, self).write(vals)
        return True

    @api.multi
    def where_used(self, vals):
#       find where product exists in BOM lines: Where Used Search
        loop_number = 0
#       loop through ALL the bom lines
        for bom_line_ids in self.env['mrp.bom.line'].search([]).ids:
#           loop through all products associated with that line (should really be only 1)
            for bom_line_product_ids in self.env['mrp.bom.line'].browse(bom_line_ids).product_id.ids:
#               find the product name and see if it matches the current product
                bom_line_product_name = self.env['mrp.bom.line'].browse(bom_line_ids).product_id.browse(bom_line_product_ids).name 
#               if the product names match loop though all the parent boms for that product. If match is found again loop will still increment and add boms.
                if bom_line_product_name == self.name:
                    for bom_ids in self.env['mrp.bom.line'].browse(bom_line_ids).bom_id.ids:
                        loop_number +=1
                        if loop_number == 1:
                            vals['sms_whereused_a_qty'] = self.env['mrp.bom.line'].browse(bom_line_ids).product_qty
                            vals['sms_whereused_a'] = bom_ids
                        if loop_number == 2:
                            vals['sms_whereused_b_qty'] = self.env['mrp.bom.line'].browse(bom_line_ids).product_qty
                            vals['sms_whereused_b'] = bom_ids
                        if loop_number == 3:
                            vals['sms_whereused_c_qty'] = self.env['mrp.bom.line'].browse(bom_line_ids).product_qty
                            vals['sms_whereused_c'] = bom_ids
                        if loop_number == 4:
                            vals['sms_whereused_d_qty'] = self.env['mrp.bom.line'].browse(bom_line_ids).product_qty
                            vals['sms_whereused_d'] = bom_ids

        super(sms, self).write(vals)
        return True



    sms_qty_forecast = fields.Float(string='Qty Forecast', related='virtual_available', readonly='True')

    sms_description_picking = fields.Char(string='Alt Stores Loc', help="Enter Alternative Stock Location", default="Additional Stock Location")
    sms_product_date = fields.Date('Date', help="Enter Date Created")
    sms_product_notes = fields.Char('Description', help="Enter Notes for SMS Employees", default="Enter detailed description for SMS Employees")
    sms_product_origin = fields.Many2one('res.partner', 'Originator')
    sms_ecoa = fields.Many2one('project.task', 'ECO 1')
    sms_ecob = fields.Many2one('project.task', 'ECO 2')
    sms_ecoc = fields.Many2one('project.task', 'ECO 3')
    sms_ecod = fields.Many2one('project.task', 'ECO 4')
    sms_ecoe = fields.Many2one('project.task', 'ECO 5')


 
