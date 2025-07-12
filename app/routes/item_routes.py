from multiprocessing.context import AuthenticationError
from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from app.services import item_service

item_bp = Blueprint('items', __name__, url_prefix='/api/items')


@item_bp.route('/', methods=['POST'])
def add_item():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing JSON Body"}), 400

        result = item_service.create_item(data=data)

        return jsonify({"message": "Item Successfully Added !!", "Item_id": str(result)}), 200

    except ValidationError as ve:
        return jsonify({"Validation Error": ve.errors()})
    except RuntimeError as re:
        return jsonify({"Runtime Error": str(re)}), 400
    except Exception as ex:
        return jsonify({"Internal Sever Error": str(ex)}), 500


@item_bp.route('/', methods=['GET'])
def get_all_items():
    try:
        items = item_service.get_all_items()
        return jsonify(items), 200

    except Exception as ex:
        return jsonify({"Internal Server Error": str(ex)}), 500

@item_bp.route('/<item_id>', methods=['GET'])
def get_item_by_id(item_id):
    try:
        item = item_service.get_item_by_id(str(item_id))

        return jsonify(item), 200

    except RuntimeError as re:
        return jsonify({"Runtime Error": str(re)}), 400
    except Exception as ex:
        return (jsonify({"Internal Server Error": str(ex)})), 500

@item_bp.route('/name/<name>', methods=['GET'])
def get_item_by_name(name):
    try:
        item = item_service.get_item_by_name(str(name))

        return jsonify(item), 200

    except RuntimeError as re:
        return jsonify({"Runtime Error": str(re)}), 400
    except Exception as ex:
        return (jsonify({"Internal Server Error": str(ex)})), 500

@item_bp.route('/<item_id>', methods=['PUT'])
def update_item_by_id(item_id):
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Missing JSON Body"}), 400


        item = item_service.update_item_by_id(item_id=item_id, item=data)

        return jsonify({"message": "Item Successfully Updated !!", "item": item}), 200

    except AuthenticationError as ae:
        return jsonify({"Authentication Error": str(ae)}), 400
    except Exception as ex:
        return jsonify({"Internal Server Error": str(ex)}), 400

@item_bp.route('/<item_id>', methods=['DELETE'])
def delete_by_id(item_id):
    try:
        result = item_service.delete_item_by_id(item_id)
        return jsonify({"message": result}), 200

    except RuntimeError as re:
        return jsonify({"Runtime Error": str(re)}), 400
    except Exception as ex:
        return jsonify({"Internal Server Error": str(ex)}), 500