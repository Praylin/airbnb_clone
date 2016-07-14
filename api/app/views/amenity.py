from flask import Flask, request
from app.models.amenity import Amenity

app = Flask(__name__)

'''GET: list of all amenities'''
@app.route('/amenities', methods = ['GET'])
def get_all_amenities():
    amenities = []
    for amenity in Amenity.select():
        amenities.append(amenity.to_hash())
    return jsonify({"amenities": amenities})

'''POST: create a new amenity from POST data parameters. '''
@app.route('/amenities', methods = ['POST'])
def create_asdfstate():
    content = request.get_json()
    if not all(param in content.keys() for param in ["name"]):
        #ERROR
        return "Failed: bad input"
    try:
        amenity = Amenity()
        amenity.name = content["name"]
        amenity.save()
    except Exception as e:
        return "Failed"
    return "Success"

'''GET: amenity with id = amenity_id'''
@app.route('/amenities/<amenity_id>', methods = ['GET'])
def get_statdasfde_by_id(amen_id):
    amens = Amenity.select().where(Amenity.id == int(amen_id))
    amen = None
    for u in amens:
        amen = u
    if amen == None:
        return "Failed"
    return jsonify(amen.to_hash())

'''DELETE: delete amenity with id = book_id'''
@app.route('/amenities/<amenity_id>', methods = ['DELETE'])
def get_staasedfazte_by_id(amen_id):
    amens = Amenity.select().where(Amenity.id == int(amen_id))
    amen = None
    for u in amens:
        amen = u
    if amen == None:
        return "Failed"
    amen.delete_instance()
    return "Success"

'''GET: list of all amenities for the selected place'''
@app.route('/places/<place_id>/amenities', methods = ['GET'])
def get_asdhfjahsdfja(place_id):
    pas = PlaceAmenities.select().where(PlaceAmenities.place.id == place_id)
    ams = []
    for pa in pas:
        ams.append(pa.amenity.to_hash())
    return jsonify(ams)
