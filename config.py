import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uKX6_E1sMzbK6D48V5-cAMaGn.Ym-eJZ.~'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsv2computer'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'DaNzzSk5cK8Nz6KFEw76OS0i+sRN6und0Hl7XgUxwn0u5YAIc+bWpZJPzfaDNhTgxu68rXZjvEFrXcXcyHpDtQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cmsv2.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'CMSV2'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'prashant_shahi'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Welcome12#'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "uKX6_E1sMzbK6D48V5-cAMaGn.Ym-eJZ.~"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    #AUTHORITY = "https://login.microsoftonline.com/438aede1-38b9-4fc2-9359-75a40a44edf2"

    CLIENT_ID = "61b0b7c8-96c8-4347-8577-19b012038256"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL for local host; must match to app's redirect_uri set in AAD
  #  REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL for Azure deployed App; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session