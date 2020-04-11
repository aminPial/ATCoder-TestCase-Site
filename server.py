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
    with urllib.request.urlopen("http://134.122.27.56:5000/contest_name") as url:
        data = json.loads(url.read().decode())
    return render_template('index.html',contest_names=[[y.lstrip().rstrip() for y in  a.split('|')]for a in  data['contest_name']],error=0)
@engine.route('/<e>')
def home2(e):
        with urllib.request.urlopen("http://134.122.27.56:5000/contest_name") as url:
            data = json.loads(url.read().decode())
        if e == "/?#":
            return render_template('index.html',contest_names=[a.split('|') for a in  data['contest_name']],error=1)
        else:
            return render_template('index.html',contest_names=[a.split('|') for a in  data['contest_name']],error=0)


if __name__ == '__main__':engine.run(host='0.0.0.0',debug=True,port=5022)


