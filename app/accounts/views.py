from django.contrib.auth import logout
from django.shortcuts import redirect


def logout(request):
    logout(request)
    1 + 1
    return redirect('lista-vendas')