{
    'name':'SMS Custom Features',
    'description':'To add SMS features to Odoo:\n\rPurchase Orders: Add Project Code\n\rContacts tree: Add details\n\rProject: Add Product and Customer\n\rEquipment: Add Customer, Warranty Expiry Date, Sales Order and Purchase Order numbers\n\rSales Orders: Adds Agent, Ship To and Invoice To fields.\n\rContact Form: Adds Event/Product Tab and SMS Data Tab\n\rProduct Form: Adds ECOs Tab and SMS Data Tab. Add Stores Location to list view',
    'author':'Robert Price',
    'depends':['mrp', 'product', 'base', 'purchase', 'sale', 'contacts', 'project', 'maintenance', 'delivery'],
    'application': True,
    'data': ['views/sms_menus.xml', 'security/ir.model.access.csv','views/sms_contacts_form_view.xml','views/sms_product_form_view.xml', 'views/sms_product_tree_view.xml','views/sms_sale_view.xml', 'views/sms_purchase_view.xml', 'views/sms_contacts_view.xml', 'views/sms_project_view.xml', 'views/sms_equipment_view.xml', 'views/sms_equipment_tree_view.xml', 'views/sms_bom_view.xml', 'views/sms_bom_tree_view.xml', 'views/sms_bom_form_view.xml' , 'views/sms_config_view.xml' ],
}
