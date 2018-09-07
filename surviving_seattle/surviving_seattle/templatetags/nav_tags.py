from django import template

from wagtail.core.models import Site

register = template.Library()

@register.inclusion_tag("tags/nav_bar.html")
def get_navbar():
    site = Site.objects.get(is_default_site=True)
    home_page = site.root_page
    pages = home_page.get_children().live().in_menu()

    return {
        "home_page": home_page,
        "pages": pages,
    }
