from django.urls import path
from .views import *
from .view_ajax import *

urlpatterns = [
    path('list/', ProdutosList.as_view(), name="produto_list"),

    path('estoque/', ListStockProducts.as_view(), name="estoque_produtos"),
    path('categorias/', CategoriaList.as_view(), name="categorias_produtos"),

    path('alterar_estoque/<int:pk>/', editar_estoque.as_view(), name="editar_estoque"),

    # ajax request ViewAddStockProduct
    path('create/',  CreateProduct.as_view(), name='create_product'),
    path('delete/<int:pk>/',  DeleteProduct.as_view(), name='delete_product'),
    path('update/<int:pk>/',  UpdateProduct.as_view(), name='update_product'),
    path('update_stock/<int:pk>/',  UpdateStockProduct.as_view(), name='update_stock'),
    path('add_stock/<int:pk>/',  AddStockProduct.as_view(), name='add_stock'),
    path('output_stock/<int:pk>/',  OutputStockProduct.as_view(), name='output_stock'),
    path('list_products/',  ListProductsAjax.as_view(), name='list_products'),
    path('stock_products/',  ListStockProductsAjax.as_view(), name='list_stock'),
    path('category_products/',  ListCategoryProductsAjax.as_view(), name='list_category'),

    path('category_create/',  CreateCategory.as_view(), name='create_category'),
    path('category_update/<int:id>/',  UpdateCategory.as_view(), name='update_category'),
    path('category_delete/<int:id>/',  DeleteCategory.as_view(), name='delete_category'),

    # views ajax
    path('view_product/<int:id>/',  ViewProduct.as_view(), name='view_product'),
    path('products_by_category/<int:id_category>',  ProductsByCategory.as_view(), name='product_by_category'),
]