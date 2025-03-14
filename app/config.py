import os

class Config:
    SECRET_KEY = os.GETENV('FLASK_SECRET_KEY', 'default_secret_key')

   
