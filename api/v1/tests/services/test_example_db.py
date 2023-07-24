import pytest

from api.v1.models.example import Example
from api.v1.services.ExampleDB import ExampleDB


# Data service text example
@pytest.fixture
def get_example_db():
    """DB instance creation"""
    db = ExampleDB([Example(name="test 1"), Example(name="test 2"), Example(name="test 3")])
    return db


def test_get_all_examples(get_example_db: ExampleDB):
    examples = get_example_db.get_all_examples()
    assert examples == [Example(name="test 1"), Example(name="test 2"), Example(name="test 3")]
