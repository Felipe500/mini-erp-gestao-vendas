from rolepermissions.roles import AbstractUserRole


class Admin(AbstractUserRole):
    available_permissions = {
        'clients_list': True,
        'clients_add_edit': True,
        'products_list': True,
        'products_add_edit': True,
        'stock_list': True,
        'stock_add_edit': True,
        'category_product_list': True,
        'category_product_add_edit': True,
        'sales_list': True,
        'sales_edit': True,
        'sales_create': True,
        'sales_cancel': True,
        'financial_movements_list': True,
        'bills_receive_list': True,
        'bills_receive_add_edit': True,
        'bills_pay_list': True,
        'bills_pay_add_edit': True,
        'settings_admin': True,
        'dashboard_sales': True,
    }


class Collaborator(AbstractUserRole):
    available_permissions = {
        'clients_list': True,
        'clients_add_edit': True,
        'products_list': True,
        'products_add_edit': True,
        'stock_list': True,
        'stock_add_edit': True,
        'category_product_list': True,
        'category_product_add_edit': True,
        'sales_list': True,
        'sales_edit': True,
        'sales_create': True,
        'sales_cancel': False,
        'financial_movements_list': True,
        'bills_receive_list': True,
        'bills_receive_add_edit': False,
        'bills_pay_list': True,
        'bills_pay_add_edit': False,
        'settings_admin': False,
        'dashboard_sales': False,
    }