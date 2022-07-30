from django import template
from django.utils.safestring import SafeString

from blog.models import Category

register = template.Library()

@register.simple_tag
def ME():
    return 'ME'


@register.inclusion_tag("blog/partial/category_nav.html")
def category_nav():
    return {
    'categories': Category.objects.filter(status=True),
    }

@register.inclusion_tag("blog/partial/current_page.html")
def current_page(request, link_name, content, classes):
    return {
        "request" : request,
        "link_name": link_name,
        "content": content,
        "link": f"account:{link_name}",
        "classes": classes,
    }


