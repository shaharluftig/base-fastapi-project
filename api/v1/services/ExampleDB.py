from typing import List

from api.v1.models.example import Example


class ExampleDB:
    """Example for data service"""

    def __init__(self, examples: List[Example]):
        self.examples = examples

    def get_all_examples(self) -> List[Example]:
        return self.examples
