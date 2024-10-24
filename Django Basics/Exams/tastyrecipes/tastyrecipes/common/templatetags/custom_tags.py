from django import template

from tastyrecipes.utils import get_user_object

register = template.Library()

@register.simple_tag
def has_profile():
    return bool(get_user_object())
