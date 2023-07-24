from cachetools.func import ttl_cache

from api.v1.models.example import Example
from api.v1.services.ExampleDB import ExampleDB


@ttl_cache(ttl=60 * 60)
def get_example_db():
    """DB instance creation"""
    db = ExampleDB([Example(name="Example 1"), Example(name="Example 2"), Example(name="Example 3")])
    return db
