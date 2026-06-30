import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URL = os.environ.get("DATABASE_URL")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    MAX_UPLOAD_SIZE_MB = int(os.environ.get("MAX_UPLOAD_SIZE_MB", "10"))
    ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "docx", "xlsx"}
    DEBUG = os.environ.get("DEBUG", "false").lower() == "true"

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
