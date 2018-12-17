from flask import Blueprint, jsonify, request
import re
import sys
from flask import Blueprint

version1 = Blueprint('apiv1',
                     __name__,
                     url_prefix='/api/v1')

users_list = []

@version1.route('/post', methods=['POST'])
def post_user():
    error = ""
    id = request.get_json()['id']
    username = request.get_json()['username']
    email = request.get_json()['email']
    password = request.get_json()['password']
    confirm_password = request.get_json()['confirm_password']

    if len(password) < 6:
        error = "Password too short"
        return jsonify(password)
    elif len(password) > 12:
        error = "Password Must be less than 12"
        return jsonify(error)
    elif not re.search("[a-z]",password):
        error = "Password Must include atleast 1 lowercase letter"
        return jsonify(error)
    elif not re.search("[0-9]",password):
        error = "Password Must include atleast 1 number"
        return jsonify(error)
    elif not re.search("[A-Z]",password):
        error = "Password Must include atleast 1 uppercase letter"
        return jsonify(error)
    elif not re.search("[$#@]",password):
        error = "Password Must include atleast 1 character"
        return jsonify(error)
    elif not re.search("[@]" ,email):
        error = "Enter a valid email"
        return jsonify(error)
    elif re.search("[@#$]" ,username):
        error = "Enter a valid username without characters"
        return jsonify(error)
    else:
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        print(pw_hash, file=sys.stdout)
        user = {
            'id':id,
            'username':username,
            'email':email,
            'password':pw_hash
        }
        users_list.append(user)
        result = jsonify({'users':users_list})
        return make_response(result,201)




@version1.route('/get', methods=['GET'])
def get_user():
    result = jsonify({"users":users_list})
    # result.status_code = 200
    return result

@version1.route('/update/<int:id>', methods=['GET'])
def update_user(id):

    for user in users_list:
        for key,value in user.items():
            print(user)


    result = jsonify(users_list)
    result.status_code = 200
    return result
