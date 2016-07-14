from flask import Flask, request
app = Flask(__name__)

'''GET: list of all cities for a state (selected by state_id)'''
@app.route('/states/<state_id>/cities', methods = ['GET'])
def get_all_cities(state_id):
    cities = []
    for city in City.select().where(City.state.id == state_id):
        cities.append(city.to_hash())
    return jsonify({"cities": cities})

'''POST: create a new city from POST data parameters in the selected state. '''
@app.route('/states/<state_id>/cities', methods = ['POST'])
def create_city():
    content = request.get_json()
    if not all(param in content.keys() for param in ["name"]):
        #ERROR
        return "Failed: bad input"
    try:
        city = City()
        city.name = content["name"]
        city.state = state_id
        city.save()
    except Exception as e:
        return "Failed"
    return "Success"

'''GET: city with id = city_id'''
@app.route('/states/<state_id>/cities/<city_id>', methods = ['GET'])
def get_state_by_id(state_id, city_id):
    if not isinstance(int(city_id), int):
        return "Failed"
    cities = Cities.select().where(city.id == int(city_id))
    city = None
    for u in cities:
        city = u
    if city == None:
        return "Failed"
    return jsonify(city.to_hash())

'''DELETE: delete city with id = city_id'''
@app.route('/states/<state_id>/cities/<city_id>', methods = ['DELETE'])
def delete_state_by_id(state_id, city_id):
    try:
        cities = Cities.select().where(city.id == int(city_id))
        city = None
        for u in cities:
            city = u
        if city == None:
            return "Failed"
        city.delete_instance()
    except:
        return "Failed"
    return "success"
