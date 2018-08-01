from django import template

register = template.Library()

# naakamaa rinda ir "decorators"
@register.filter(name='cut')

def cut(value,arg):
    """
    This custs out all values of "arg" from the string!
    """
    return value.replace(arg, '')

# register.filter('cut',cut)
# sho rindu aizstaajam ar python decorators
