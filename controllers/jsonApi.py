from flask import Blueprint, jsonify
from helpers.dbHelper import (getCategoryByName,
                              getItemByName, getAllCatalogItems)

jsonApiController = Blueprint('api/json', __name__)


@jsonApiController.route('/')
def viewAllJSON():
    """
    Send details about all the Categories
    and their respective Items in the database
    """
    allItems = getAllCatalogItems()
    return jsonify([i.serialize for i in allItems])


@jsonApiController.route('/<string:category_name>')
def viewCategoryJSON(category_name):
    """
    Send details about the category specified in category_name
    """
    category = getCategoryByName(category_name)
    return jsonify(category.serialize)


@jsonApiController.route('/<string:category_name>/<string:item_name>')
def viewItemJSON(category_name, item_name):
    """
    Send details about the item specified in item_name.
    Category_name present for API aesthetics but not used.
    """
    item = getItemByName(item_name)
    return jsonify(item.serialize)
