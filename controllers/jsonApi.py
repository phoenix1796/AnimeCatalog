from flask import Blueprint, jsonify
from helpers.dbHelper import getCategoryByName, getItemByName

jsonApiController = Blueprint('api/json', __name__)


@jsonApiController.route('/<string:category_name>')
def viewCategoryJSON(category_name):
    category = getCategoryByName(category_name)
    return jsonify(category.serialize)


@jsonApiController.route('/<string:category_name>/<string:item_name>')
def viewItemJSON(category_name, item_name):
    item = getItemByName(item_name)
    return jsonify(item.serialize)
