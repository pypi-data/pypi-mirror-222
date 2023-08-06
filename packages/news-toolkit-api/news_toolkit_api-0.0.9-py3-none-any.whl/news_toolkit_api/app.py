from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi_injector import attach_injector
from injector import Injector

from news_toolkit_api.api.v1.routers import router


def create_app(injector: Injector) -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    attach_injector(app, injector)

    @app.get("/robots.txt", response_class=PlainTextResponse)
    def robots():
        return "User-agent: *\nDisallow: /"

    return app
