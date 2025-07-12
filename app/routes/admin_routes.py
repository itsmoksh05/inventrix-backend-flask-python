from flask import Blueprint, jsonify
from app.services import admin_service

admin_bp = Blueprint('admin', __name__, url_prefix='/api/admin')


@admin_bp.route('/users', methods=['GET'])
def get_all_users():
    try:
        users = admin_service.get_all_users()

        if users is None:
            return jsonify({"message": "No User Found !!"}), 200

        return jsonify(users), 200

    except Exception as ex:
        return jsonify({"message": "Internal Server Error:" + str(ex)})


@admin_bp.route('/user/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    try:
        user = admin_service.get_user_by_id(user_id=user_id)

        return jsonify(user), 200
    except RuntimeError as re:
        return jsonify({"message": "Runtime Error:" + str(re)}), 400
    except Exception as ex:
        return jsonify({"message": "Internal Server Error:" + str(ex)}), 500


@admin_bp.route('/user/<user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    try:
        result = admin_service.delete_user_by_id(user_id=user_id)

        return jsonify({"message": result}), 200
    except RuntimeError as re:
        return jsonify({"message": "Runtime Error:" + str(re)}), 400
    except Exception as ex:
        return jsonify({"message": "Internal Server Error:" + str(ex)}), 500
