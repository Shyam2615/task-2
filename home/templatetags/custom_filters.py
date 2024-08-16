from django import template

register = template.Library()

@register.filter
def truncate_summary(value, word_limit=15):
    if not value:
        return ''
    
    words = value.split()
    if len(words) > word_limit:
        return ' '.join(words[:word_limit]) + '...'
    return value
