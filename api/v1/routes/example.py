from typing import List

from fastapi import APIRouter, Depends

from api.v1 import deps
from api.v1.helpers.logger import logger
from api.v1.models.example import Example
from api.v1.services.ExampleDB import ExampleDB

example_router = APIRouter(tags=["example"])


@example_router.get("/", response_model=List[Example])
def get_all_examples(example_db: ExampleDB = Depends(deps.get_example_db)) -> List[Example]:
    """Returns all examples"""
    logger.info("example log")
    return example_db.get_all_examples()
