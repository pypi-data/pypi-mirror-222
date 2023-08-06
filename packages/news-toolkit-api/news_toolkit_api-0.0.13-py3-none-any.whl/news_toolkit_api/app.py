from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from injector import Injector

from news_toolkit_api.api.v1.routers import router


def create_app(injector: Injector) -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    app.state.injector = injector

    @app.get("/robots.txt", response_class=PlainTextResponse)
    def robots():
        return "User-agent: *\nDisallow: /"

    return app
