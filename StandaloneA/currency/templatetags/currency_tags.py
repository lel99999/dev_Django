from django import template

register = template.Library()

@register.filter
def accounting(value):
    return "({0}".format(value) if value < 0 else "{0}".format(value)
