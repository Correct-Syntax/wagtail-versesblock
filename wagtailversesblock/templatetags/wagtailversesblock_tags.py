from django.template import Library
from django.utils.safestring import mark_safe


register = Library()


def bold_verse_numbers(verses):
    verse_html = ""

    # FIXME: would be nice if it only added the <b> tag 
    # around the numbers as a whole (e.g: <b>12</b>), not 
    # individually (e.g: <b>1</b><b>2</b>) -but this works.
    for char in sorted(range(0, 9), reverse=True):
        verse_html = verses.replace(
            str(char), "<b>{}</b>".format(char)
        )
        verses = verse_html

    return mark_safe(verses)

register.filter('bold_verse_numbers', bold_verse_numbers)