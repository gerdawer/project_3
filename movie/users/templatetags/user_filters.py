from django import template
# В template.Library зарегистрированы все теги и филдьтры шаблонов
# добавляем ещё один фильтр
register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})
