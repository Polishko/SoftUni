from django import template
from django.core.exceptions import ImproperlyConfigured

register = template.Library()
# 1. user provided by the tag function that gets the context as arg
@register.inclusion_tag('posts/../../../templates/common/user_info.html', takes_context=True)
def user_info(context):
    request = context.get('request')

    if not request:
        raise ImproperlyConfigured(
            "Request object is missing from context.")

    user = getattr(request, 'user', None)

    result = user.username if user and user.is_authenticated else 'Anonymous'

    return {
        'username': result
    }

# 2. user provided by the relevant template
# @register.inclusion_tag('posts/common/user_info.html')
# def user_info(user):
#
#     result = user.username if user and user.is_authenticated else 'Anonymous'
#
#     return {
#         'username': result
#     }


