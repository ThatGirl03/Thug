import os

class Config:
    import os

SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')


   
