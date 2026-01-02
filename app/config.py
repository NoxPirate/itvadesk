import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-in-prod")
    # MySQL connection using pymysql
    # DB_USER = os.environ.get("DB_USER", "root")
    # DB_PASS = os.environ.get("DB_PASS", "")   # default XAMPP = empty
    # DB_HOST = os.environ.get("DB_HOST", "localhost")
    # DB_NAME = os.environ.get("DB_NAME", "supportdesk")
    
    # SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    
    # SQLite configuration
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mail Configuration
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "itvadesk@gmail.com"
    MAIL_PASSWORD = "jdffvrnipwmwtoeb"
    MAIL_DEFAULT_SENDER = "itvadesk@gmail.com"


