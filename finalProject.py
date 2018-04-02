from flask import session as login_session
from flask import (Flask, abort, flash, jsonify, redirect, render_template,
                   request, send_from_directory, url_for)

from controllers.authController import authController
from controllers.jsonApi import jsonApiController
from helpers.authHelper import login_required
from helpers.dbHelper import (CatalogItem, Category, getAllCategories,
                              getCategoryByName, getItemByName,
                              getItemsByCategory, session)
from helpers.securityHelper import csrf_protect, generate_csrf_token

app = Flask(__name__)


app.before_request(csrf_protect)


@app.route('/')
@app.route('/catalog/')
def viewCatalog():
    return render_template('catalog.html', categoryList=getAllCategories(), loggedIn='1' if 'user_id' in login_session else '0')


@app.route('/catalog/<string:category_name>/items')
def viewCategory(category_name):
    categoryList = getAllCategories()
    myCategory = getCategoryByName(category_name)
    catalogItems = session.query(CatalogItem).filter_by(
        category_id=myCategory.id)
    return render_template('catalog.html', categoryList=categoryList,
                           category=myCategory,
                           items=catalogItems,
                           loggedIn='1' if 'user_id' in login_session else '0')


@app.route('/catalog/<string:category_name>/<string:item_name>')
def viewItem(category_name, item_name):
    myCategory = getCategoryByName(category_name)
    catalogItems = getItemsByCategory(myCategory)
    item = session.query(CatalogItem).filter_by(name=item_name).one()

    if 'user_id' not in login_session:
        return render_template('publicItem.html',
                               category=myCategory,
                               items=catalogItems,
                               anime=item)

    return render_template('item.html',
                           category=myCategory,
                           items=catalogItems,
                           anime=item,
                           itemCreator='1' if login_session['user_id'] == item.user_id else '0',
                           categoryCreator='1' if login_session['user_id'] == myCategory.user_id else '0')


@app.route('/catalog/<string:category_name>/<string:item_name>/edit', methods=['GET', 'POST'])
@login_required
def editItem(category_name, item_name):
    item = getItemByName(item_name)
    if item.user_id != login_session['user_id']:
        return "<body onload='alert(\"Forbidden Access.\")'>"

    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
            item.summary = request.form['summary']
            item.category = getCategoryByName(request.form['category'])
            session.add(item)
            session.commit()
            return redirect(url_for('viewItem', category_name=item.category.name, item_name=item.name))
    else:
        return render_template('EditItem.html', CategoryList=getAllCategories(), Category=category_name, Item=item)


@app.route('/catalog/new/category', methods=['GET', 'POST'])
@login_required
def newCategory():
    if request.method == 'POST':
        newCategory = Category(
            user_id=login_session['user_id'], name=request.form['name'], summary=request.form['summary'])
        session.add(newCategory)
        session.commit()
        return redirect(url_for('viewCatalog'))
    else:
        return render_template('newCategory.html', CategoryList=getAllCategories())


@app.route('/catalog/new/item', methods=['GET', 'POST'])
@login_required
def newItem():
    if request.method == 'POST':
        newItem = CatalogItem(user_id=login_session['user_id'], name=request.form['name'],
                              summary=request.form['summary'], category=getCategoryByName(request.form['category']))
        session.add(newItem)
        session.commit()
        return redirect(url_for('viewItem', category_name=newItem.category.name, item_name=newItem.name))
    else:
        if request.args.get('category_name'):
            return render_template('newItem.html', CategoryList=getAllCategories(), Category=request.args.get('category_name'))
        return render_template('newItem.html', CategoryList=getAllCategories())


@app.route('/catalog/<string:category_name>/delete', methods=['GET', 'POST'])
@login_required
def deleteCategory(category_name):
    Category = getCategoryByName(category_name)
    if Category.user_id != login_session['user_id']:
        return "<body onload='alert(\"Forbidden Access.\")'>"

    if request.method == 'POST':
        session.delete(Category)
        session.commit()
        return redirect(url_for('viewCatalog'))
    else:
        return render_template('deleteCategory.html', Category=Category.name)


@app.route('/catalog/<string:category_name>/<string:item_name>/delete', methods=['GET', 'POST'])
@login_required
def deleteItem(category_name, item_name):
    item = getItemByName(item_name)
    if item.user_id != login_session['user_id']:
        return "<body onload='alert(\"Forbidden Access.\")'>"

    if request.method == 'POST':
        session.delete(item)
        session.commit()
        return redirect(url_for('viewCategory', category_name=category_name))
    else:
        return render_template('deleteItem.html', Item=item_name, Category=category_name)


if __name__ == '__main__':
    app.jinja_env.globals['csrf_token'] = generate_csrf_token
    app.register_blueprint(jsonApiController, url_prefix='/api/json')
    app.register_blueprint(authController)
    app.secret_key = 'shitaki-mushrooms!'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
