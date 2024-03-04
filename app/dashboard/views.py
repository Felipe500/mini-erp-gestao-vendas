from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from app.sales.models import Sale


class DashboardView(LoginRequiredMixin, View):

    def get(self, request):
        data = {'media': Sale.statistic.media(),
                'media_desc': Sale.statistic.media_desconto(),
                'min': Sale.statistic.min(),
                'max': Sale.statistic.max(),
                'n_ped': Sale.statistic.num_pedidos()}
        return render(request, 'vendas/dashboard.html', data)