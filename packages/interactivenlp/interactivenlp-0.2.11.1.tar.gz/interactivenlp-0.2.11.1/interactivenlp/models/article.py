from typing import List, Optional

from .block import Block


class Article:
    def __init__(self, title: str, url: str, blocks: Optional[List['Block']] = None, global_block: Optional['Block'] = None):
        self.title = title
        self.url = url
        self.blocks = blocks
        self.global_block = global_block

    def copy(self):
        return Article(self.title, self.url, self.blocks, self.global_block)
