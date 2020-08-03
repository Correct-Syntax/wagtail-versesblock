from wagtail.core.blocks import (
    CharBlock,
    StructBlock,
    StructValue,
    TextBlock
)
from django.utils.safestring import mark_safe


class VersesBlock(StructBlock):
    def __init__(self, local_blocks=None, **kwargs):

        if local_blocks is None:
            local_blocks = []
        else:
            local_blocks = local_blocks.copy()

        local_blocks.extend([
            ('caption', 
            CharBlock(
                help_text='Reference to where the verses are found in the Bible.',
                )
            ),
            ('verses', TextBlock()),
        ])

        super().__init__(local_blocks, **kwargs)

    class Meta:
        icon = "doc-full"
        template = 'wagtailversesblock/verses_block.html'
