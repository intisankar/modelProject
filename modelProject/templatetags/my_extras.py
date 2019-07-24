"""
    This is custom filter file
"""
from django import template

register =template.Library()

# method2:using decoretors
@register.filter(name="cut")
def cut(value,arg):
    """
    this cuts out all the value of 'arg' from the string
    """
    return value.replace(arg,'')

# method 1: using  normal call
# register.filter('cut',cut)

# Synatax: register filter ('string(name)',methodname)
