from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag(takes_context=True)
def current_time(context, format_string):
    return datetime.now().strftime(format_string)


@register.filter
def get_range(value):
    return range(value)


@register.simple_tag
def cabecalho_nova_venda():
    return 'NOVA VENDA'


@register.simple_tag
def cabecalho_editar_venda():
    return 'DETALHES DA VENDA'


@register.simple_tag
def text_bt_nova_venda():
    return 'CRIAR VENDA'


@register.simple_tag
def text_bt_editar_venda():
    return 'ATUALIZAR CABEÇALHO DA VENDA'


@register.simple_tag
def footer_message():
    return 'Desenvolvimento web com Django 2.0.2'
