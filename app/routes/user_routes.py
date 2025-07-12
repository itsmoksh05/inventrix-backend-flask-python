from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from pymongo.errors import DuplicateKeyError
from app.services import user_service

user_bp = Blueprint("auth", __name__, url_prefix='/api/auth')


@user_bp.route('/register', methods=['POST'])
def add_user():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"runtime error": "Missing JSON Body"}), 400

        result = user_service.create_user(data=data)

        return jsonify({"message": "User Successfully Created !!", "result": str(result)}), 201

    except DuplicateKeyError as de:
        return jsonify({"error": str(de)}), 400

    except ValidationError as ve:
        return jsonify({"validation error": ve.errors()}), 400

    except Exception as e:
        return jsonify({"internal server Error": str(e)}), 500


@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Empty JSON Body"}), 400

    try:

        if user_service.verify_user(data.get('username'), data.get('password')):
            return jsonify({"message": "Logged in Successfully !!"}), 200

    except RuntimeError as re:
        return jsonify({"Runtime Error": str(re)}), 400

    except Exception as ex:
        return jsonify({"Internal Server Error": str(ex)}), 500
    return jsonify({"message": "success"})


""" 
    !!! TO BE AUTHENTICATED !!! 
"""


@user_bp.route('/me/<username>', methods=['GET'])
def get_my_profile(username):
    if not username:
        return jsonify({"error": "Username is Missing !!"}), 400

    try:
        user = user_service.get_my_profile(str(username))
        final_user = {
            "username": user.get('username'),
            "email": user.get('email'),
            "role": user.get('role')
        }
        return jsonify(final_user), 200

    except RuntimeError as re:
        return jsonify({"Runtime Error": str(re)}), 400

    except Exception as ex:
        return jsonify({"Internal Server Error": str(ex)}), 500
