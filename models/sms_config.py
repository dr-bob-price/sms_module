# -*- coding: utf-8 -*-
from odoo import models
from odoo import fields
from odoo import api

class sms(models.Model):
    _name = 'sms.config'
    name = fields.Char('Name', required=True)
    descrip = fields.Char('Description', required=False)
    value = fields.Float('Value', required=False, readonly='True')
    parts = fields.Float('Part Count', required=False, readonly='True')
    date = fields.Date('Date')
    bom_number = fields.Integer('Nos of BOMs', readonly='True')

    def find_where_used(self):

        for n in self.env['product.template'].search([]):
            loop_number = 0
#           loop through ALL the bom lines
            for bom_line_ids in self.env['mrp.bom.line'].search([]).ids:
#               loop through all products associated with that line (should really be only 1)
                for bom_line_product_ids in self.env['mrp.bom.line'].browse(bom_line_ids).product_id.ids:
#                   find the product name and see if it matches the current product
                    bom_line_product_name = self.env['mrp.bom.line'].browse(bom_line_ids).product_id.browse(bom_line_product_ids).name 
#                   if the product names match, loop though all the parent boms for that product. If a match is found again loop will still increment and add boms.
                    if bom_line_product_name == n.name:
                        for bom_ids in self.env['mrp.bom.line'].browse(bom_line_ids).bom_id.ids:
                            loop_number +=1
                            if loop_number == 1:
                                n.sms_whereused_a_qty = self.env['mrp.bom.line'].browse(bom_line_ids).product_qty
                                n.sms_whereused_a = bom_ids
                            if loop_number == 2:
                                n.sms_whereused_b_qty = self.env['mrp.bom.line'].browse(bom_line_ids).product_qty
                                n.sms_whereused_b = bom_ids
                            if loop_number == 3:
                                n.sms_whereused_c_qty = self.env['mrp.bom.line'].browse(bom_line_ids).product_qty
                                n.sms_whereused_c = bom_ids
                            if loop_number == 4:
                                n.sms_whereused_d_qty = self.env['mrp.bom.line'].browse(bom_line_ids).product_qty
                                n.sms_whereused_d = bom_ids
        return True

    def update_bom_cost(self):
        bom_nos = 0
        for k in self.env['mrp.bom'].search([]):
            bom_nos +=1
            line_cost = 0
            total = 0
            for l in k.bom_line_ids.ids:
                line_product_id = k.bom_line_ids.browse(l).product_id.ids
                line_product_cost = k.bom_line_ids.browse(l).product_id.browse(line_product_id).sms_cost
                line_cost = k.bom_line_ids.browse(l).product_qty * line_product_cost
                total = total + line_cost
            k.sms_bom_cost=total 
        self.bom_number = bom_nos
        return True


    def update_stock_value(self):
        total = 0
        part_count=0
        for n in self.env['product.template'].search([]):

            n.sms_cost= n.standard_price

            uom_id = n.uom_po_id.ids
            uom_factor = n.uom_po_id.browse(uom_id).factor_inv

            prod_cat_id = n.categ_id.ids
            product_cat = n.categ_id.browse(prod_cat_id).name

            start=0

            for m in n.seller_ids.ids:

                sellerid = n.seller_ids.browse(m).name.ids
                ex_rate_id = n.seller_ids.browse(m).currency_id.ids
                exchange_rate = n.seller_ids.browse(m).currency_id.browse(ex_rate_id).rate

                if start == 0:
                    start = (n.seller_ids.browse(m).price/uom_factor)/exchange_rate
                    n.sms_supplier = n.seller_ids.browse(m).name.browse(sellerid).name
                    loop=0
                    for o in sellerid:
                        loop+=1
                        if loop == 1:
                            n.sms_supplierb=o
                    n.sms_cost = start
                price = (n.seller_ids.browse(m).price/uom_factor)/exchange_rate
                if price > start:
                    n.sms_cost = price
                    start = price

            bom_ids = self.env['mrp.bom'].search([]).ids
            for record in bom_ids:
                bom_name = self.env['mrp.bom'].browse(record).product_tmpl_id.name
                if bom_name == n.name:
                    n.sms_cost = self.env['mrp.bom'].browse(record).sms_bom_cost

            if n.sms_cost > 0:
                n.standard_price = n.sms_cost

            sms_factor = 2.22
            if product_cat == 'Accessories':
                sms_factor = 3.33
            if product_cat == 'Consumables':
                sms_factor = 2.86
            if product_cat == 'Systems':
                sms_factor = 4
            if product_cat == 'Service':
                sms_factor = 1

            n.list_price = n.sms_cost * sms_factor
            n.sms_stock_value = n.qty_available * n.sms_cost
            part_count = part_count + n.qty_available
            total = total + n.sms_stock_value
            

        self.value=total
        self.parts = part_count



        return True
