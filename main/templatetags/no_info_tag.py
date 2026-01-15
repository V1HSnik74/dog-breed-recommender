from django import template

register = template.Library()

@register.filter
def no_info(value):
    return 'Нет информации' if value == 0 else f'{value}/5'