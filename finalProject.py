from flask import Flask,render_template,url_for,send_from_directory,request,redirect,flash,jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CatalogItem
from data import categories,items

app = Flask(__name__)

#db setup
engine = create_engine("sqlite:///catalog.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

categories = [
    {'name':'snoweestuff','description':'cvfs','summary':'lorem lorem lorem loremlorem loremlorem loremloremlorem lorem lorem'},
    {'name':'land stuff','description':'fe','summary':'ipsum ipsum ipsum ipsum ipsum ipsum ipsum ipsumipsum ipsum ipsum ipsum ipsum ipsum'}]

singleCategory =     {'name':'snoweestuff','description':'cvfs','summary':'lorem lorem lorem loremlorem loremlorem loremloremlorem lorem lorem'}
items = [
        {'name':'Snowboard','category':'snoweestuff','summary':'loremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsum'},
        {'name':'skateboard','category':'land stuff','summary':'loremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumasdff'}
        ]

singleItem = {'id':'1','name':'skateboard','category':'land stuff','summary':'loremipsumloremipsumloremipsumloremipsumloremipsumloremipsumlorem ipsumloremipsumloremipsumasdff'}

def getAllCategories():
    return session.query(Category).with_entities(Category.name).all()
def getCategoryByName(name):
    print(name)
    return session.query(Category).filter_by(name = name).one()

def getItemsByCategory(category):
    return session.query(CatalogItem).filter_by(category_id = category.id)

def getItemByName(item_name):
    return session.query(CatalogItem).filter_by(name = item_name).one()
@app.route('/')
@app.route('/catalog/')
def showCatalog():
    return render_template('catalog.html', categoryList = getAllCategories())

@app.route('/catalog/<string:category>/items')
def viewCategory(category):
    categoryList = getAllCategories()
    myCategory = getCategoryByName(category)
    catalogItems = session.query(CatalogItem).filter_by(category_id = myCategory.id)
    return render_template('catalog.html', categoryList = categoryList, 
                                            category = myCategory,
                                            items=catalogItems)

@app.route('/catalog/<string:category>/items/JSON')
def viewCategoryJSON(category):
    return "Category JSON for the category %s" % category

@app.route('/catalog/<string:category_name>/<string:item_name>')
def viewItem(category_name, item_name):
    myCategory = getCategoryByName(category_name)
    catalogItems = getItemsByCategory(myCategory)
    item = session.query(CatalogItem).filter_by(name = item_name).one()
    return render_template('item.html', category = myCategory, items = catalogItems, anime = item)

@app.route('/catalog/<string:category>/<string:item>/JSON')
def viewItemJSON(category, item):
    return "JSON for item : %s in category : %s" % (item ,category)

@app.route('/catalog/<string:category>/<string:item>/delete', methods = ['GET','POST'])
def deleteItem(category, item):
    return "delete item : %s in category : %s" % (item ,category)

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
            print("asdasdsadsadsad:\n",item.category.name)
            return redirect(url_for('viewItem', category_name=item.category.name, item_name=item.name))
    else:
        return render_template('EditItem.html',CategoryList = getAllCategories(),Category = category_name, Item = item)

@app.route('/catalog/new/category', methods = ['GET','POST'])
def newCategory():
    return "Create a new category page"

@app.route('/catalog/new/item', methods = ['GET','POST'])
def newItem():
    return "Create a new item page"

if __name__=='__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.secret_key = 'shuck!'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)