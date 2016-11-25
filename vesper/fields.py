import bleach

from django.db.models.fields import TextField
from django.utils.encoding import smart_text

from .widgets import RichTextareaWidget


class RichTextarea(TextField):
    """
    """

    def to_python(self, value):
        """
        """
        if value:
            html = value.replace('&nbsp;', ' ')
            html = smart_text(html.encode('utf-8'))

            ALLOWED_TAGS = [
                'p',
                'br',

                'i',
                'strong',
                'b',

                'ul',
                'li',
                'ol',

                'table',
                'tr',
                'th',
                'td',
            ]

            ALLOWED_ATTRIBUTES = {
            }

            html = bleach.clean(html, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES, strip=True)
            return html
        else:
            return value

    def formfield(self, **kwargs):
        kwargs['widget'] = RichTextareaWidget
        return super(RichTextarea, self).formfield(**kwargs)