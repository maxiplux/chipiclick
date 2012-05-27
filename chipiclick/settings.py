from chipiclick.settings import  *
import os.path,locale,sys

PROJECT_DIR = os.path.dirname(__file__)

PROJECT_PATH = os.path.abspath(PROJECT_DIR)

ADMINS = (
# ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '%s/database.db'% PROJECT_PATH,                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'OPTIONS':{"timeout": 20},
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}