from django.template import Library, Context
from django.template.loader import get_template

register = Library()

@register.simple_tag
def list_filter_render(spec):
    tpl = get_template(spec.template)
    return tpl.render(Context({
        'title': spec.title,
        'choices': list(spec.choices()),
        'spec': spec,
        }))