from flask import Flask, request
app = Flask(__name__)

'''GET: list of all users'''
@app.route('/users', methods=['GET'])
def get_all_users():
    users = []
    for user in User.select():
        users.append(user.to_hash())
    return jsonify({"users": users})

'''POST: create a new user from POST data parameters'''
@app.route('/users', methods=['POST'])
def create_user():
    content = request.get_json()
    if not all(param in content.keys() for param in ["email", "password", "first_name", "last_name", "is_admin"]):
        #ERROR
        return "Failed: bad input"
    try:
        user = User()
        user.email = content["email"]
        user.first_name = content["first_name"]
        user.last_name = content["last_name"]
        user.is_admin = content["is_admin"]
        user.set_password(content["password"])
        user.save()
    except Exception as e:
        print e
        return "Failed"
    return "Success"

'''GET: user with id = user_id'''
@app.route('/users/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    if not isinstance(int(user_id), int):
        return "Failed"
    users = User.select().where(User.id == int(user_id))
    user = None
    for u in users:
        user = u
    if user == None:
        return "Failed"
    return jsonify(user.to_hash())

'''PUT: update the user with id = user_id with PUT data parameters.'''
@app.route('/users/<user_id>', methods=['PUT'])
def update_user_by_id(user_id):
    def update_password(user, newpass):
        user.set_password(newpass)

    def update_first_name(user, newname):
        user.first_name = newname

    def update_last_name(user, newname):
        user.last_name = newname

    def update_admin(user, newrights):
        user.is_admin = newrights

    try:
        content = request.get_json()
        users = User.select().where(User.id == int(user_id))
        user = None
        for u in users:
            user = u
        if user == None:
            return "Failed"
        for param in content.keys():
            try:
                {
                    "password": update_password,
                    "first_name": update_first_name,
                    "last_name": update_last_name,
                    "is_admin": update_admin,
                }[param](user, content[param])
            except NameError:
                pass
        user.save()
    except:
        return "Failed"
    return jsonify(user.to_hash())

'''DELETE: delete user with id = user_id'''
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    try:
        users = User.select().where(User.id == int(user_id))
        user = None
        for u in users:
            user = u
        if user == None:
            return "Failed"
        user.delete_instance()
    except:
        return "Failed"
    return "success"
