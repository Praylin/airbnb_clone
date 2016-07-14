from flask import Flask, request
app = Flask(__name__)

'''GET: list of all states'''
@app.route('/states', methods = ['GET'])
def get_all_states():
    states = []
    for state in State.select():
        states.append(state.to_hash())
    return jsonify({"states": states})

'''POST: create a new state from POST data parameters.'''
@app.route('/states', methods = ['POST'])
def create_state():
    content = request.get_json()
    if not all(param in content.keys() for param in ["name"]):
        #ERROR
        return "Failed: bad input"
    try:
        state = State()
        state.name = content["name"]
        state.save()
    except Exception as e:
        return "Failed"
    return "Success"

'''GET: state with id = state_id'''
@app.route('/states/<state_id>', methods = ['GET'])
def get_statedddd_by_id(state_id):
    if not isinstance(int(state_id), int):
        return "Failed"
    states = State.select().where(State.id == int(state_id))
    state = None
    for u in states:
        state = u
    if state == None:
        return "Failed"
    return jsonify(state.to_hash())

'''DELETE: delete state with id = state_id'''
@app.route('/states/<state_id>', methods = ['DELETE'])
def delete_statedddd_by_id(state_id):
    try:
        states = State.select().where(State.id == int(state_id))
        state = None
        for u in states:
            state = u
        if state == None:
            return "Failed"
        state.delete_instance()
    except:
        return "Failed"
    return "success"
