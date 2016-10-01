from django import template
import markdown

register = template.Library()


@register.filter
def markdownify(text):
    """
    Used to render in a insecure fashion the message markdown text.
    Since the message text is not escaped the app is vulnerable to XSS.
    """
    return markdown.markdown(text)
