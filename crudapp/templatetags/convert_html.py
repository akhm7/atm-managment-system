from django import template

register = template.Library()

@register.filter
def convert_html(value):
    return value.replace("&lt;br/&gt;","\n")