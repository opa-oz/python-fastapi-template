from fastapi import FastAPI

from contextlib import asynccontextmanager

from .config import get_config, Config

global_stores = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the config
    cfg = get_config()
    global_stores["cfg"] = cfg
    yield
    # Clean up the clients and release the resources
    global_stores.clear()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root(name: str = '<unknown>'):
    cfg: Config = global_stores["cfg"]

    if not cfg.prod:
        name = 'dev_' + name

    return {'name': name}


@app.get("/healz")
async def healz():
    return {"message": "OK"}


@app.get("/ready")
async def ready():
    return {"message": "Ready"}
