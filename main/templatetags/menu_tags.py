from django import template
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context.get('request')  # Получаем объект request из контекста
    if not request:
        raise ValueError("Request object is required in context")

    current_url = request.path
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')

    def build_menu_tree(parent=None):
        items = menu_items.filter(parent=parent)
        tree = []
        for item in items:
            children = build_menu_tree(item)
            tree.append({
                'item': item,
                'children': children,
                'active': current_url.startswith(item.get_absolute_url()),
                'expand': any(current_url.startswith(child.get_absolute_url()) for child in children)
            })
        return tree

    return {'menu': build_menu_tree()}
