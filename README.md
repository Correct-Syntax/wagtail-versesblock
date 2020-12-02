Wagtail Verses Block
====================

Simple and easy-to-setup Bible verse highlighter/formatter streamfield block for Wagtail CMS. Useful for quoting Scripture verses in a blog post, etc.


# Screenshots

!["Wagtail verses block result"](https://github.com/Correct-Syntax/wagtail-versesblock/blob/master/screenshots/wagtailversesblock-block-result.jpg?raw=true "Wagtail verses block result")

!["Wagtail verses block admin"](https://github.com/Correct-Syntax/wagtail-versesblock/blob/master/screenshots/wagtailversesblock-block-admin.jpg?raw=true "Wagtail verses block admin")


# Usage

Install via pip:

``pip install wagtailversesblock``

Import and add ``VersesBlock`` to *models.py*:

```python

...

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
...
from wagtailversesblock.blocks import VersesBlock

...

class ExamplePage(Page):

    ...

    body = StreamField([
        ('verses', VersesBlock()),
    ], null=True)

```


# Development

Pull requests and/or feature suggestions are welcome!


# License

Licensed under the BSD 3-Clause license