from flask import Flask,render_template,url_for,send_from_directory,request,redirect,flash,jsonify
from jsonApi import jsonApi
from dbHelper import *

import random,string
from flask import session as login_session
from flask import make_response
import json
import httplib2
import requests

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

app = Flask(__name__)

CLIENT_ID = json.loads(
open('client_secrets.json', 'r').read())['web']['client_id']

@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state, CLIENT_ID=CLIENT_ID)

@app.route('/gconnect', methods = ['POST'])
def gconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid State parameter'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    code = request.data
    try:
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(json.dumps('Failed to upgrade the Auth code'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    
    if result.get('error') is not None:
        reponse = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    #Verify if Access Token is for the intended user
    gPlusId = credentials.id_token['sub']
    if result['user_id'] != gPlusId:
        response = make_response(
            json.dumps('Token Id | User Id Mismatch')
        , 401)
        response.headers['Content-Type'] = 'application/json'
        return response        

    #Verify Access token is for the intended Application
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps('Token\'s Client Id | App Id Mismatch')
        , 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    #Check if user already logged In
    storedCredentials = login_session.get('credentials')
    storedGPlusId = login_session.get('gplus_id')
    if storedCredentials is not None and gPlusId == storedGPlusId:
        response = make_response(
            json.dumps('User already logged in')
        , 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    
    login_session['credentials'] = credentials.to_json()
    login_session['gplus_id'] = gPlusId

    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token , 'alt':'json'}
    answer = requests.get(userinfo_url, params = params)
    data = json.loads(answer.text)

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output= "WOWZA!"
    return output

@app.route('/gdisconnect')
def gdisconnect():
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(json.dumps('Current User not connected') , 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    access_token = json.loads(credentials)['access_token']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token

    h = httplib2.Http()
    result = h.request(url, 'GET')
    if result[0]['status'] == '200':
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
    
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response

@app.route('/')
@app.route('/catalog/')
def viewCatalog():
    return render_template('catalog.html', categoryList = getAllCategories())

@app.route('/catalog/<string:category_name>/items')
def viewCategory(category_name):
    categoryList = getAllCategories()
    myCategory = getCategoryByName(category_name)
    catalogItems = session.query(CatalogItem).filter_by(category_id = myCategory.id)
    return render_template('catalog.html', categoryList = categoryList, 
                                            category = myCategory,
                                            items=catalogItems)

@app.route('/catalog/<string:category_name>/<string:item_name>')
def viewItem(category_name, item_name):
    myCategory = getCategoryByName(category_name)
    catalogItems = getItemsByCategory(myCategory)
    item = session.query(CatalogItem).filter_by(name = item_name).one()
    return render_template('item.html', category = myCategory, items = catalogItems, anime = item)

@app.route('/catalog/<string:category_name>/<string:item_name>/edit', methods = ['GET','POST'])
def editItem(category_name, item_name):
    print(login_session)
    if 'username' not in login_session:
        return redirect('/login')
    item = getItemByName(item_name)
    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
            item.summary = request.form['summary']
            item.category = getCategoryByName(request.form['category'])
            session.add(item)
            session.commit()
            return redirect(url_for('viewItem', category_name=item.category.name, item_name=item.name))
    else:
        return render_template('EditItem.html',CategoryList = getAllCategories(),Category = category_name, Item = item)

@app.route('/catalog/new/category', methods = ['GET','POST'])
def newCategory():
    if 'username' not in login_session:
        return redirect('/login')

    if request.method == 'POST':
        newCategory = Category(name = request.form['name'], summary = request.form['summary'])
        session.add(newCategory)
        session.commit()
        return redirect(url_for('viewCatalog'))
    else:
        return render_template('newCategory.html', CategoryList = getAllCategories())

@app.route('/catalog/new/item', methods = ['GET','POST'])
def newItem():
    if 'username' not in login_session:
        return redirect('/login')

    if request.method == 'POST':
        newItem = CatalogItem(name = request.form['name'], summary = request.form['summary'],category = getCategoryByName(request.form['category']))
        session.add(newItem)
        session.commit()
        return redirect(url_for('viewItem', category_name = newItem.category.name, item_name = newItem.name))
    else:
        if request.args.get('category_name'):
            return render_template('newItem.html', CategoryList = getAllCategories(), Category = request.args.get('category_name'))
        return render_template('newItem.html', CategoryList = getAllCategories())

@app.route('/catalog/<string:category_name>/delete', methods = ['GET','POST'])
def deleteCategory(category_name):
    if 'username' not in login_session:
        return redirect('/login')

    if request.method == 'POST':
        item = session.query(Category).filter_by(name = category_name).one()
        session.delete(item)
        session.commit()
        return redirect(url_for('viewCatalog'))
    else:
        return render_template('deleteCategory.html', Category = category_name)

@app.route('/catalog/<string:category_name>/<string:item_name>/delete', methods = ['GET','POST'])
def deleteItem(category_name, item_name):
    if 'username' not in login_session:
        return redirect('/login')

    if request.method == 'POST':
        item = session.query(CatalogItem).filter_by(name = item_name).one()
        session.delete(item)
        session.commit()
        return redirect(url_for('viewCategory', category = category_name))
    else:
        return render_template('deleteItem.html', Item = item_name, Category = category_name)

if __name__=='__main__':
    app.register_blueprint(jsonApi, url_prefix='/api/json')
    app.secret_key = 'shitaki-mushrooms!'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)