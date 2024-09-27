# pip install markdown

import markdown
from django import template
from django.utils.safestring import mark_safe

# mark_safe: called before each filter and escapes the provided tags to prevent injections
# you can still use italic tag/mark_safe converts it

register = template.Library()

# we register a filter named markdown in our library
@register.filter(name='markdown')
def markdown_format(text):
    # markdown.markdown adds the markdown
    return mark_safe(markdown.markdown(text))