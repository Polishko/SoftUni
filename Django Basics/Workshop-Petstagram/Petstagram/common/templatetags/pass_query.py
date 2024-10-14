from django import template

register = template.Library()

@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()  # Get the current query parameters
    dict_[field] = value  # Update the specified field with the new value
    return dict_.urlencode()  # Return the updated query string
