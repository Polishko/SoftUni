from django import template

register = template.Library()

@register.simple_tag
def has_three_or_more(value):
    return value >= 3


@register.simple_tag
def has_zero(value):
    return value == 0
