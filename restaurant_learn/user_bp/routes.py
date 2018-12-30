from flask import Blueprint, render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook
from oauthlib.oauth2.rfc6749.errors import InvalidGrantError, TokenExpiredError, OAuth2Error
import os

user_bp = Blueprint('user_bp', __name__)

google_bp = make_google_blueprint(
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    scope=[
        "https://www.googleapis.com/auth/plus.me",
        "https://www.googleapis.com/auth/userinfo.email",
    ]
)


@user_bp.route('/login/')
def login():
    print(os.getenv('GOOGLE_CLIENT_ID'))
    return render_template('login.html')


@user_bp.route('/login/google/')
def login_google():

    if not google.authorized:
        print(url_for('google.login'))
        return redirect(url_for('google.login'))
    try:
        resp = google.get('/oauth2/v2/userinfo')
        assert resp.ok, resp.text
    except(TokenExpiredError):
        return redirect(url_for('google.login'))

    return f'''You are {resp.json()['email'} on Google'''
