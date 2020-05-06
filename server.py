from flask import *
import urllib.request, json
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://3f40025957e040ec820dc8e300d7ebb8@o361561.ingest.sentry.io/5196832",
    integrations=[FlaskIntegration()]
)

from string import ascii_uppercase
engine=Flask(__name__)
@engine.route('/')
def home():
    return render_template('index.html')
