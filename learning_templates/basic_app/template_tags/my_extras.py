from django import template

register = template.Library()
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from string!
    """
    return value.replace(arg,'')

#register.filter('cut',cut)
#first is the name of the function and second is the call to the function.Here in the above line we are not using decorators

#Now below line uses decorators
    

