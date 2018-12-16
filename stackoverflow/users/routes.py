from flask import Blueprint, jsonify, request

users = Blueprint('users',__name__,url_prefix='/users')
users_list = []

@users.route('/post', methods=['POST'])
def post_user():
    name = request.get_json('name')
    city = request.get_json('city')

    user = {
        'name':name,
        'city':city
    }
    users_list.append(user)
    result = jsonify(users_list)
    result.status_code = 201
    return result

@users.route('/get', methods=['GET'])
def get_user():
    result = jsonify(users_list)
    result.status_code = 200
    return result
