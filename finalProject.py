from flask import Flask,render_template,url_for,send_from_directory,request,redirect,flash,jsonify
from jsonApi import jsonApi
from dbHelper import *

app = Flask(__name__)

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
    if request.method == 'POST':
        newCategory = Category(name = request.form['name'], summary = request.form['summary'])
        session.add(newCategory)
        session.commit()
        return redirect(url_for('viewCatalog'))
    else:
        return render_template('newCategory.html', CategoryList = getAllCategories())

@app.route('/catalog/new/item', methods = ['GET','POST'])
def newItem():
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
    if request.method == 'POST':
        item = session.query(Category).filter_by(name = category_name).one()
        session.delete(item)
        session.commit()
        return redirect(url_for('viewCatalog'))
    else:
        return render_template('deleteCategory.html', Category = category_name)

@app.route('/catalog/<string:category_name>/<string:item_name>/delete', methods = ['GET','POST'])
def deleteItem(category_name, item_name):
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