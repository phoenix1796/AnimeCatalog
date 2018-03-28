from flask import Blueprint,json
from dbHelper import *

jsonApi = Blueprint('api/json', __name__)

@jsonApi.route('/<string:category>')
def viewCategoryJSON(category):
    return "Category JSON for the category %s" % category

@jsonApi.route('/<string:category>/<string:item>')
def viewItemJSON(category, item):
    return "JSON for item : %s in category : %s" % (item ,category)
