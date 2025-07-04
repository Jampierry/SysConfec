# Filtro customizado para moeda brasileira
from django import template
register = template.Library()

@register.filter
def brl(value):
    try:
        value = float(value)
        return f'R$ {value:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    except:
        return value
