from django import template

register = template.Library()

@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()  # Get the current query parameters and copy {'pet_name': 'george'}
    dict_[field] = value  # Add the new field and value to dict {'pet_name': 'george', 'page': 2}
    return dict_.urlencode()  # Return the updated query string ?pet_name=george&page=2
