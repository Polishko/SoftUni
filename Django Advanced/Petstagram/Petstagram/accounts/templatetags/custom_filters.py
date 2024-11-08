from django import template

register = template.Library()


@register.filter
def placeholder(value, token):
    # value is our object that we place the filter on
    # token is the placeholder text
    value.field.widget.attrs['placeholder'] = token
    return value
