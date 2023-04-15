import os

try:
    from config_secrets import key, admin_email, azure_email, azure_mail_connection_string
except ImportError:
    key = admin_email = azure_email = azure_mail_connection_string = None

SECRET_KEY = os.getenv("SECRET_KEY", key)
ADMIN_EMAIL_ADDRESS = os.getenv("ADMIN_EMAIL_ADDRESS", admin_email)
AZURE_EMAIL_ADDRESS = os.getenv("AZURE_EMAIL_ADDRESS", azure_email)
AZURE_MAIL_CONNECTION_STRING = os.getenv("AZURE_MAIL_CONNECTION_STRING", azure_mail_connection_string)