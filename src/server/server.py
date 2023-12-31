import logging
from typing import Optional

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from starlette.background import BackgroundTasks
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from src.shared.enum.exception_info import ExceptionInfoValue, ExceptionInfo
from src.utils.config_parser import parser

from src.server.router.image_classification_router import router as classifier_router


class ErrorResponseContent:
    def __init__(self, key: str = None, message: str = None):
        self.key = key
        self.message = message


class ErrorResponse(JSONResponse):
    def __init__(self, content: ErrorResponseContent, code: int = 500,
                 background: Optional[BackgroundTasks] = None):
        super().__init__(content, code, background=background)

    def render(self, content: any) -> bytes:
        return super().render(vars(content))


def _get_error_response(e: ExceptionInfoValue, msg: str) -> ErrorResponse:
    return ErrorResponse(
        ErrorResponseContent(e.key, msg),
        e.code
    )


async def _exception_handler_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        exception = ExceptionInfo.UNKNOWN_ERROR.value
        return _get_error_response(exception, str(e))
    except ValidationError as e:
        exception = ExceptionInfo.VALIDATION_ERROR.value
        return _get_error_response(exception, str(e))


class Server:
    def __init__(self):
        self.logger = logging.getLogger('Server')
        docs = "/docs" if int(parser.get_attr('server', 'docs')) else None
        redoc = "/redoc" if int(parser.get_attr('server', 'redoc')) else None
        allowed_origins = parser.get_attr('server', 'allow_origins').split(',')
        allowed_methods = parser.get_attr('server', 'allow_methods').split(',')
        allowed_headers = parser.get_attr('server', 'allow_headers').split(',')
        self.prefix = parser.get_attr('server', 'prefix')
        self.app = FastAPI(docs_url=docs, redoc_url=redoc)
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=allowed_origins,
            allow_credentials=True,
            allow_methods=allowed_methods,
            allow_headers=allowed_headers,
        )
        self.app.middleware("http")(_exception_handler_middleware)
        self.app.add_exception_handler(RequestValidationError, self.validation_exception_handler)
        self.routers = [classifier_router]

    def prepare(self):
        prefix = self.prefix if self.prefix else '/api/v1'
        for router in self.routers:
            self.app.include_router(router, prefix=prefix)

    async def validation_exception_handler(self, _: Request, e: RequestValidationError):
        self.logger.error(str(e.errors()))
        return _get_error_response(ExceptionInfo.VALIDATION_ERROR.value, str(e).replace('\n', ''))
