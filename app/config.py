import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'B9k0u8cdRkHe_HVAsdYdFeJKYVE6M2zM4Q4NGJZ3zvA')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False