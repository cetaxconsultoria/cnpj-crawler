from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def isnone(dictionary, key):
    if dictionary.get(key) != None:
        return mark_safe('<li>'+key+': '+dictionary.get(key)+'</li>')
    else:
        return ''

@register.filter
def secundarias(dictionary):
    atividades = '<li>Atividade Secundária: '+dictionary.get('Atividade Secundária')+'</li>'
    for i in range(1,11):
        if dictionary.get('Atividade Secundária_'+str(i)) != None:
            atividades += '<li>Atividade Secundária: '+dictionary.get('Atividade Secundária_'+str(i))+'</li>'
    return mark_safe(atividades)

@register.filter
def socios(dictionary):
    if dictionary.get('Sócio') != None:
        socios = '<h4>Quadro de Sócios</h4><ul>'
        socios += '<li>Sócio: '+dictionary.get('Sócio')+'</li>'
        for i in range(1,6):
            if dictionary.get('Sócio_'+str(i)) != None:
                socios += '<li>Sócio: '+dictionary.get('Sócio_'+str(i))+'</li>'
        socios += '</ul>'
        return mark_safe(socios)
    else:
        return ''

@register.filter
def modulo(num, val):
    return (num+1) % val
