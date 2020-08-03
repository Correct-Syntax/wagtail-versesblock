Wagtail Verses Block
====================

Bible verse highlighter/formatter streamfield block for Wagtail CMS.


# Usage

Import and add ``VersesBlock`` to *models.py*:

```python

...

from wagtail.core.models import Page
from wagtail.core.fields import StreamField

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