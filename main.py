from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import HTTPException

from static_pages.router import static_pages_router, templates


load_dotenv()

async def not_found_error(request: Request, exc: HTTPException):
    return templates.TemplateResponse('static_pages/templates/404.html', {'request': request}, status_code=404)

async def internal_server_error(request: Request, exc: HTTPException):
    return templates.TemplateResponse('static_pages/templates/500.html', {'request': request}, status_code=500)

exception_handlers = {
    404: not_found_error,
    500: internal_server_error
}

app = FastAPI(docs_url=None, redoc_url=None, exception_handlers=exception_handlers)
app.mount("/static", StaticFiles(directory="static_pages/static"), name="static")

app.include_router(static_pages_router, tags=["pages"], prefix="")
