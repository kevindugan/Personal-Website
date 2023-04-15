from .app import app
import os
from azure.functions import HttpRequest, HttpResponse, Context, WsgiMiddleware

# Configuration
try:
    from .config_secrets import key, admin_email, azure_email, azure_mail_connection_string
except ImportError:
    key = admin_email = azure_email = azure_mail_connection_string = None
app.config.update(
    SECRET_KEY = os.getenv("SECRET_KEY", key),
    ADMIN_EMAIL_ADDRESS = os.getenv("ADMIN_EMAIL_ADDRESS", admin_email),
    AZURE_EMAIL_ADDRESS = os.getenv("AZURE_EMAIL_ADDRESS", azure_email),
    AZURE_MAIL_CONNECTION_STRING = os.getenv("AZURE_MAIL_CONNECTION_STRING", azure_mail_connection_string)
)

def main(req: HttpRequest, context: Context) -> HttpResponse:
    return WsgiMiddleware(app.wsgi_app).handle(req, context)