from flask import Blueprint, render_template, make_response, request, redirect
from flask import session as login_session

from helpers.dbHelper import *

import random
import string
import json
import httplib2
import requests

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

GOOGLE_PLUS_SECRETS = 'secrets/client_secrets.json'

authController = Blueprint('authController', __name__)

CLIENT_ID = json.loads(
    open(GOOGLE_PLUS_SECRETS, 'r').read())['web']['client_id']


@authController.route('/login')
def login():
    if 'username' in login_session:
        if request.args.get('next'):
            return redirect(request.args.get('next'))
        else:
            return redirect('/')
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state, CLIENT_ID=CLIENT_ID)


@authController.route('/gconnect', methods=['POST'])
def gconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid State parameter'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    code = request.data
    try:
        oauth_flow = flow_from_clientsecrets(GOOGLE_PLUS_SECRETS, scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(json.dumps(
            'Failed to upgrade the Auth code'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check if the token received is a valid token
    access_token = credentials.access_token
    url = (credentials.token_info_uri + "?access_token=%s" % access_token)
    response = requests.get(url)
    result = response.json()

    if result.get('error') is not None:
        reponse = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify if Access Token is for the intended user
    gPlusId = credentials.id_token['sub']
    if result['sub'] != gPlusId:
        response = make_response(
            json.dumps('Token Id | User Id Mismatch'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify Access token is for the intended Application
    if result['aud'] != CLIENT_ID:
        response = make_response(
            json.dumps('Token\'s Client Id | App Id Mismatch'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check if user already logged In
    storedCredentials = login_session.get('credentials')
    storedGPlusId = login_session.get('gplus_id')
    if storedCredentials is not None and gPlusId == storedGPlusId:
        response = make_response(
            json.dumps('User already logged in'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    login_session['credentials'] = credentials.to_json()
    login_session['gplus_id'] = gPlusId

    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = json.loads(answer.text)

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # Check if user already exists
    userId = getUserId(login_session['email'])
    if userId is None:
        userId = createUser(login_session)

    login_session['user_id'] = userId

    output = "WOWZA!"
    return redirect('/')


@authController.route('/gdisconnect')
def gdisconnect():
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(json.dumps('Current User not connected'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    credentials = json.loads(credentials)
    access_token = credentials['access_token']
    url = credentials['revoke_uri']

    result = requests.post(url, params={'token': access_token}, headers={
                           'content-type': 'application/x-www-form-urlencoded'})
    # print(result.status_code)

    if result.status_code == 200:
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']

        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps(
            'Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response
