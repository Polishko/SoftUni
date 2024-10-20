from django import template

register = template.Library()

@register.simple_tag()
def has_profile(request):
    return request.session.get('has_profile', False)