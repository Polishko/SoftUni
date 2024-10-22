from django import template

from musicapp.utils import get_user_object

register = template.Library()

@register.simple_tag
def has_profile():
    profile = get_user_object()
    return bool(profile)
