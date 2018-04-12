from flask import session as login_session
from flask import (Flask, abort, flash, jsonify, redirect, render_template,
                   request, send_from_directory, url_for)

from controllers.authController import authController, getGplusClientId
from controllers.jsonApi import jsonApiController
from helpers.authHelper import login_required
from helpers.dbHelper import (CatalogItem, Category, getAllCategories,
                              getCategoryByName, getItemByName,
                              getItemsByCategory, session)
from helpers.securityHelper import (csrf_protect, generate_csrf_token,
                                    generate_login_token)

app = Flask(__name__)


@app.route('/')
@app.route('/catalog/')
def viewCatalog():
    """
    Serve the overview of the catalog
    """
    return render_template('catalog.html', categoryList=getAllCategories())


@app.route('/catalog/<string:category_name>/items')
def viewCategory(category_name):
    """
    View all items of the specified category_name
    """
    categoryList = getAllCategories()
    myCategory = getCategoryByName(category_name)
    catalogItems = session.query(CatalogItem).filter_by(
        category_id=myCategory.id)
    return render_template('catalog.html', categoryList=categoryList,
                           category=myCategory,
                           items=catalogItems)


@app.route('/catalog/<string:category_name>/<string:item_name>')
def viewItem(category_name, item_name):
    """
    View details about the specific item_name belonging to category_name
    """
    myCategory = getCategoryByName(category_name)
    catalogItems = getItemsByCategory(myCategory)
    item = session.query(CatalogItem).filter_by(name=item_name).one()

    return render_template('item.html',
                           category=myCategory,
                           items=catalogItems,
                           anime=item)


@app.route(
    '/catalog/<string:category_name>/<string:item_name>/edit',
    methods=[
        'GET',
        'POST'])
@login_required
@csrf_protect
def editItem(category_name, item_name):
    """
    Edit item details of Item:item_name belonging to Category:category_name
    """
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
            return redirect(
                url_for(
                    'viewItem',
                    category_name=item.category.name,
                    item_name=item.name))
    else:
        return render_template(
            'EditItem.html',
            CategoryList=getAllCategories(),
            Category=category_name,
            Item=item)


@app.route('/catalog/<string:category_name>/edit', methods=['GET', 'POST'])
@login_required
@csrf_protect
def editCategory(category_name):
    """
    Edit details about the Category: category_name
    """
    category = getCategoryByName(category_name)
    if category.user_id != login_session['user_id']:
        return "<body onload='alert(\"Forbidden Access.\")'>"

    if request.method == 'POST':
        if request.form['name']:
            category.name = request.form['name']
            category.summary = request.form['summary']
            session.add(category)
            session.commit()
            return redirect(
                url_for(
                    'viewCategory',
                    category_name=category.name))
    else:
        return render_template('EditCategory.html', Category=category)


@app.route('/catalog/new/category', methods=['GET', 'POST'])
@login_required
@csrf_protect
def newCategory():
    """
    Create a new category
    """
    if request.method == 'POST':
        newCategory = Category(
            user_id=login_session['user_id'],
            name=request.form['name'],
            summary=request.form['summary'])
        session.add(newCategory)
        session.commit()
        return redirect(url_for('viewCatalog'))
    else:
        return render_template(
            'newCategory.html',
            CategoryList=getAllCategories())


@app.route('/catalog/new/item', methods=['GET', 'POST'])
@login_required
@csrf_protect
def newItem():
    """
    Create a new CatalogItem
    """
    if request.method == 'POST':
        newItem = CatalogItem(
            user_id=login_session['user_id'],
            name=request.form['name'],
            summary=request.form['summary'],
            category=getCategoryByName(
                request.form['category']))
        session.add(newItem)
        session.commit()
        return redirect(
            url_for(
                'viewItem',
                category_name=newItem.category.name,
                item_name=newItem.name))
    else:
        if request.args.get('category_name'):
            return render_template(
                'newItem.html',
                CategoryList=getAllCategories(),
                Category=request.args.get('category_name'))
        return render_template('newItem.html', CategoryList=getAllCategories())


@app.route('/catalog/<string:category_name>/delete', methods=['GET', 'POST'])
@login_required
@csrf_protect
def deleteCategory(category_name):
    """
    Delete an existing Category: category_name
    """
    Category = getCategoryByName(category_name)
    if Category.user_id != login_session['user_id']:
        return "<body onload='alert(\"Forbidden Access.\")'>"

    if request.method == 'POST':
        session.delete(Category)
        session.commit()
        return redirect(url_for('viewCatalog'))
    else:
        return render_template('deleteCategory.html', Category=Category.name)


@app.route(
    '/catalog/<string:category_name>/<string:item_name>/delete',
    methods=[
        'GET',
        'POST'])
@login_required
@csrf_protect
def deleteItem(category_name, item_name):
    """
    Delete an existing Item: item_name
    """
    item = getItemByName(item_name)
    if item.user_id != login_session['user_id']:
        return "<body onload='alert(\"Forbidden Access.\")'>"

    if request.method == 'POST':
        session.delete(item)
        session.commit()
        return redirect(url_for('viewCategory', category_name=category_name))
    else:
        return render_template(
            'deleteItem.html',
            Item=item_name,
            Category=category_name)


if __name__ == '__main__':
    app.jinja_env.globals['csrf_token'] = generate_csrf_token
    app.jinja_env.globals['login_token'] = generate_login_token
    app.jinja_env.globals['CLIENT_ID'] = getGplusClientId()
    app.register_blueprint(jsonApiController, url_prefix='/api/json')
    app.register_blueprint(authController)
    app.secret_key = '0d784e7a-3d71-11e8-b467-0ed5f89f718b'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
