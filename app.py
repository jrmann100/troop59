#!/home/flask/venv/bin/python
from flask import Flask, send_from_directory, render_template, jsonify, request, Response, url_for
import os
from functools import wraps

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'secret'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated



# Index Page.

@app.route('/')
def index():
    return render_template('index.html')

# Reading .txt file.
@app.route('/static/<path:path>')
def send_file(path):
    return send_from_directory(os.path.join(app.root_path, 'static'), path)


@app.route('/communications/<path:path>')
def render_commpage(path):
    return render_template('communications/' + path)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9001)
