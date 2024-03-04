from model_utils import Choices

TYPE_USER = Choices(('admin', 'Administrador(a)'), ('businessperson', 'Empresario(a)'), ('employee', 'Funcionario(a)'))

MOVEMENTS = Choices(
    ('account_paid', 'Conta Paga'),
    ('account_received', 'Conta Recebida'),
    ('sale', 'Concluida Venda'),
    ('expenses', 'Despesas'),
)

TYPE_MOVEMENT = Choices(
    ('0', 'Saida'),
    ('1', 'Entrada')
)

TIPO_MOVIMENTO_FILTER = Choices(
    ('', 'Todos'),
    ('0', 'saida'),
    ('1', 'entrada')
)
FORMA_PG = Choices(
    ('1', 'ESPECIE'),
    ('2', 'PIX'),
    ('3', 'CARTAO'),
    ('4', 'ESPECIE E PIX'),
    ('5', 'ESPECIE E CARTÃO'),
    ('6', 'PIX E CARTÃO'),
    ('7', 'ESPECIE, PIX E CARTÃO'),
)

CONTA_A_PAGAR = Choices(
    ('1', 'CONTA DE ENERGIA'),
    ('2', 'CONTA DE AGUÁ'),
    ('3', 'CONTA DE INTERNET'),
    ('4', 'SALÁRIO FUNCIONÁRIO'),
    ('5', 'PAGAMENTO FORNECEDOR'),
    ('6', 'IMPOSTOS E TRIBUTOS'),
)

CONTA_A_RECEBER = Choices(
    ('1', 'DOAÇÃO'),
    ('2', 'CONTA DE AGUÁ'),
    ('3', 'CONTA DE INTERNET'),
    ('4', 'SALÁRIO FUNCIONÁRIO'),
    ('5', 'PAGAMENTO FORNECEDOR'),
    ('6', 'IMPOSTOS E TRIBUTOS'),
)

STATUS_PAYMENT_A_PAGAR = Choices(
    ('pay', 'Pago'),
    ('not_pay', 'A Pagar')
)

STATUS_PAYMENT_A_RECEBER = Choices(
    ('pay', 'Recebido'),
    ('not_received', 'A Receber')
)

FILTER_CONTA_A_PAGAR = Choices(
    ('0', 'TODAS'),
    ('1', 'CONTA DE ENERGIA'),
    ('2', 'CONTA DE AGUÁ'),
    ('3', 'CONTA DE INTERNET'),
    ('4', 'SALÁRIO FUNCIONÁRIO'),
    ('5', 'PAGAMENTO FORNECEDOR'),
    ('6', 'IMPOSTOS E TRIBUTOS'),
)

FILTER_CONTA_A_RECEBER = Choices(
    ('0', 'TODAS'),
    ('1', 'DOAÇÃO'),
    ('2', 'CONTA DE AGUÁ'),
    ('3', 'CONTA DE INTERNET'),
    ('4', 'SALÁRIO FUNCIONÁRIO'),
    ('5', 'PAGAMENTO FORNECEDOR'),
    ('6', 'IMPOSTOS E TRIBUTOS'),
)

FILTER_STATUS_PAYMENT_A_PAGAR = Choices(
    ('0', 'TODAS'),
    ('pay', 'Pago'),
    ('not_pay', 'A Pagar')
)

FILTER_STATUS_PAYMENT_A_RECEBER = Choices(
    ('0', 'TODAS'),
    ('pay', 'Recebido'),
    ('not_received', 'A Receber')
)

STATUS_SALE = Choices(
    ('not_pay', 'Aguardando Pagamento'),
    ('paid', 'Pago'),
    ('cancel', 'Cancelado')
)

SET_PERMISSION = Choices(
    (0, 'Não permitido'),
    (1, 'Permitido')
)


PERMISSIONS = [
    ('app_clients_list', 'Visualizar Lista de Clientes'),
    ('app_clients_view', 'Ver dados do cliente'),
    ('app_clients_create', 'Criar novo Cliente'),
    ('app_clients_change', 'Alterar Cliente'),
    ('app_clients_delete', 'Apagar Cliente'),

    ('app_products', 'Gerenciar produtos'),
    ('app_products_view', 'Visualizar produtos'),

    ('app_stock', 'Gerenciar estoque'),
    ('app_stock_view', 'Visualizar estoque'),

    ('app_category_product', 'Gerenciar Categoria de Produto'),
    ('app_category_product_view', 'Visualizar Categoria de Produto'),

    ('app_sales', 'Gerenciar vendas'),
    ('app_sales_view', 'Visualizar vendas'),
    ('app_sales_edit', 'Editar vendas'),
    ('app_sales_cancel', 'Cancelar vendas'),

    ('app_bills_receive', 'Gerenciar Contas a receber'),
    ('app_bills_receive_view', 'Visualizar  Contas a receber'),

    ('app_bills_pay', 'Gerenciar  Contas a pagar'),
    ('app_bills_pay_view', 'Visualizar  Contas a pagar'),

    ('app_financial_movements', 'Gerenciar movimentações'),

    ('settings_admin', 'Configurações do Administrador'),
    ('dashboard_sales', 'Visualizar Painel de Vendas'),


]