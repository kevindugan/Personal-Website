from .app import app
from azure.functions import HttpRequest, HttpResponse, Context, WsgiMiddleware

def main(req: HttpRequest, context: Context) -> HttpResponse:
    return WsgiMiddleware(app.wsgi_app).handle(req, context)