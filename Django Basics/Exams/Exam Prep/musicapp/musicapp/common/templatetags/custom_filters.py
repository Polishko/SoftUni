from django import template

register = template.Library()

@register.filter(name='titlecase')
def titlecase(value):
    return ' '.join([word.lower().capitalize() for word in value.split()])
