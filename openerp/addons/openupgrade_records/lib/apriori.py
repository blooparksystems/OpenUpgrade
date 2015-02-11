""" Encode any known changes to the database here
to help the matching process
"""

renamed_modules = {
    'base_calendar': 'calendar',
    'mrp_jit': 'procurement_jit',
    # OCA/account-invoicing
    'invoice_validation_wkfl': 'account_invoice_validation_workflow',
    'profile_leaserad': 'lr_report',
    'sale_dropshipping': 'lr_stock_dropshipping',
}

renamed_models = {
}
