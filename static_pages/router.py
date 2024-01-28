from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
import datetime

static_pages_router = APIRouter()
templates = Jinja2Templates(directory="")

@static_pages_router.get('/')
def index(request: Request):
    return templates.TemplateResponse(
        'static_pages/templates/index.html',
        context={'request': request })


@static_pages_router.get('/privacy')
def index(request: Request):
    return templates.TemplateResponse(
        'static_pages/templates/privacy.html',
        context={
            'request': request})


@static_pages_router.get('/terms-of-service')
def index(request: Request):
    return templates.TemplateResponse(
        'static_pages/templates/terms_of_service.html',
        context={
            'request': request})


@static_pages_router.get('/sitemap.xml')
def index(request: Request):
    b = request.base_url
    urls = list()
    urls.append({'loc': b, 'lastmod': datetime.date.today()})


    return templates.TemplateResponse(
        'static_pages/templates/sitemap.xml',
        media_type='application/xml',
        context={
            'request': request,
            'urls': urls})


@static_pages_router.get('/robots.txt')
def index(request: Request):
    return templates.TemplateResponse(
        'static_pages/templates/robots.txt',
        media_type='text/plain',
        context={
            'request': request,
            'sitemap_url': f"{request.base_url}sitemap.xml"})
