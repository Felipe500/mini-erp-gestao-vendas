from django.test import TestCase
from app.vendas.models import Venda, ItemsVenda
from app.produtos.models import Produto
from app.clientes.models import Cliente
from django.contrib.auth import get_user_model
from app.produtos.models import Estoque
from .data_test import *
User = get_user_model()

# UserDetails.objects.create(**{"name":"A", "place": loc})


class VendaTestCase(TestCase):
    def setUp(self):
        """CONFIGURAÇÃO DE TESTES"""
        self.user = User.objects.create_user(**user_test)
        self.client = Cliente.objects.create(vendedor_cadastro=self.user, **cliente_test)
        self.venda = Venda.objects.create(cliente=self.client, vendedor=self.user, desconto=10)
        self.produto = Produto.objects.create(descricao='produto 1', preco=10)

    def test_01_verifica_estoque(self):
        """VERIFICAR O ESTOQUE DO PRODUTO"""
        print('test 01 - VERIFICAR O ESTOQUE DO PRODUTO')
        assert Estoque.objects.filter(produto=self.produto).count() == 1

    def test_02_verifica_num_vendas(self):
        """TESTE DE NUMERO DE VENDAS"""
        print('test 02 - TESTE DE NUMERO DE VENDAS')
        assert Venda.objects.all().count() == 1

    def test_03_add_produtos_venda(self):
        """ADICIONAR PRODUTOS NA VENDA"""
        print('test 03 - ADICIONAR PRODUTOS NA VENDA')
        ItemsVenda.objects.create(venda=self.venda, produto=self.produto, quantidade=10, desconto=10)
        assert self.venda.valor == 80

    def test_04_inclusao_lista_itens(self):
        """VERIFICAR SE ITENS ESTÃO SENDO INCLUSOS"""
        print('test 04 - VERIFICAR SE ITENS ESTÃO SENDO INCLUSOS')
        item = ItemsVenda.objects.create(
        venda=self.venda, produto=self.produto, quantidade=1, desconto=0)
        self.assertIn(item, self.venda.itemsvenda_set.all())

    def test_05_status_nfe(self):
        """VERIFICAR STATUS NFE: PADRAO FALSE"""
        print('test 05 - VERIFICAR STATUS NFE: PADRAO FALSE')
        self.assertFalse(self.venda.nfe_emitida)

    def test_06_status_venda(self):
        """ ALTERAR DE STATUS DA VENDA"""
        print('test 06 - ALTERAR DE STATUS DA VENDA')
        self.venda.status = 'FE'
        self.venda.save()
        self.assertEqual(self.venda.status, 'FE')





