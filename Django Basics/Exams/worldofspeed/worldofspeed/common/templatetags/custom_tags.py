from django import template

from worldofspeed.utils import get_user_object

register = template.Library()

@register.simple_tag
def has_profile():
    return bool(get_user_object())
