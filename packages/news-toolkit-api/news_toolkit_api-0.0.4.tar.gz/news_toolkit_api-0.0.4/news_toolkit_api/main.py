from fastapi import FastAPI
from fastapi_injector import attach_injector
from injector import Injector

from news_toolkit_api.api.v1.routers import router


def create_app(injector: Injector) -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    attach_injector(app, injector)
    return app


inj = Injector()
app = create_app(inj)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5555, reload=True)
