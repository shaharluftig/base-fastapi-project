import uvicorn
from fastapi import FastAPI

from api.v1.api import v1_router
from api.v1.config import config

app = FastAPI()

app.include_router(v1_router, prefix="/v1")


@app.get("/")
async def is_alive() -> str:
    return "I'm running"


def main():
    uvicorn.run("server:app", host=config.host, port=config.port, reload=config.reload, workers=config.workers)


if __name__ == '__main__':
    main()
