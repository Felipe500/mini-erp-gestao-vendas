from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),

    path('', include('app.dashboard.urls'), name='dashboard'),
    path('clientes/', include('app.customers.urls')),
    path('produtos/', include('app.products.urls')),
    path('vendas/', include('app.sales.urls')),
    path('controle_contas/', include('app.financial_control.urls')),
    path('settings/', include('app.settings.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

AdminSite.site_header = "Gestão de Vendas"
AdminSite.site_title = "Seja bem-vindo"
AdminSite.index_title = "Administração"

