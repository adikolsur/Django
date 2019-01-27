from django import template

register=template.Library()

@register.filter(name='cut_string')
def cut_string(value,arg):
    return value.replace(arg,'')

#register.filter('cut_string',cut_string)