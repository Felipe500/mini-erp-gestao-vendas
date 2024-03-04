JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Dash Mini ERP",
    # "site_logo": "config/static/Cover.png",
    # Title on the brand, and login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Mini ERP",
    # Welcome text on the login screen
    "welcome_sign": "Bem vindo ao Mini ERP",
    # Copyright on the footer
    "copyright": "Felipe ®",
    "show_sidebar": True,
    "navigation_expanded": True,
    "user_avatar":  "fas fa-user",
    "icons": {
        "accounts.user": "fas fa-user",
        "accounts.admin": "fas fa-user-cog",
        "accounts.businessperson": "fas fa-users",
        "accounts.collaborator": "fas fa-address-book",
        "auth.group": "fa fa-users",
        "clients.Client": "fas fa-address-book",
        "companies.Company": "fa fa-university",
        "companies.UserCompany": "fa fa-address-card",
        "products.category": "fa fa-cubes",
        "products.product": "fa fa-cube",
        "products.stock": "fas fa-boxes",
        "sales.Sale": "fas fa-chart-bar",
        "sales.ItemsSale": "fas fa-edit",
        "settings.Maq_Cartao": "far fa-credit-card",
        "financial_control.Movements": "fas fa-money-bill",
        "financial_control.BillsReceive": "fas fa-hand-holding-usd",
        "financial_control.BillsPay": "fas fa-hand-holding-usd",
    },

    "order_with_respect_to": [
        "dashboard",
        "accounts",
        "auth",
        "companies",
        "clients"
        "financial_control",
        "products",
        "sales",
        "settings"
    ],
}