from flask import Flask, request
from app.models.place import Place
from app.models.user import User
from app.models.place_book import PlaceBook

app = Flask(__name__)

'''GET: list of all books for the selected place (by place_id)'''
@app.route('/places/<place_id>/books', methods = ['GET'])
def get_all_bookings(place_id):
    books = []
    for book in PlaceBook.select().where(PlaceBook.place.id == place_id):
        books.append(book.to_hash())
    return jsonify({"books": books})

'''POST: create a new book from POST data parameters (user should be set by ID) for the selected place.'''
@app.route('/places/<place_id>/books', methods = ['POST'])
def create_new_booking(place_id):
    content = request.get_json()
    if not all(param in content.keys() for param in ["user", "is_validated", "date_start", "number_nights"]):
        #ERROR
        return "Failed: bad input"
    try:
        users = User.select().where(User.id == int(user_id))
        user = None
        for u in users:
            user = u
        if user == None:
            return "Failed, user does not exist"

        places = Place.select().where(Place.id == int(place_id))
        place = None
        for u in places:
            place = u
        if place == None:
            return "Failed, place does not exist"

        placebook = PlaceBook()
        placebook.user = user
        placebook.place = place
        placebook.is_validated = content["is_validated"]
        placebook.date_start = content["date_start"]
        placebook.number_nights = content["number_nights"]
        placebook.save()
    except Exception as e:
        return "Failed"
    return "Success"

'''GET: book with id = book_id'''
@app.route('/places/<place_id>/books/<book_id>', methods = ['GET'])
def get_book_by_id(place_id, book_id):
    books = PlaceBook.select().where(PlaceBook.id == int(book_id))
    book = None
    for u in books:
        book = u
    if book == None:
        return "Failed"
    return jsonify(book.to_hash())

'''PUT: update the book with id = book_id with PUT data parameters. '''
@app.route('/places/<place_id>/books/<book_id>', methods = ['PUT'])
def update_placebook_by_id(place_id, book_id):
    def update_place(book, place_id):
        places = Place.select().where(Place.id == int(place_id))
        place = None
        for u in places:
            place = u
        if place == None:
            return "Failed, place does not exist"
        book.place = place

    def update_valid(book, val):
         book.is_validated = val

    def update_date(book, val):
        book.date_start = val

    def update_nights(book, val):
        book.number_nights = val

    try:
        content = request.get_json()
        books = PlaceBook.select().where(PlaceBook.id == int(book_id))
        book = None
        for u in books:
            book = u
        if book == None:
            return "Failed"
        for param in content.keys():
            try:
                {
                    "place": update_place,
                    "is_validated": update_valid,
                    "date_start": update_date,
                    "number_nights": update_nights,
                }[param](book, content[param])
            except NameError:
                pass
        book.save()
    except:
        return "Failed"
    return jsonify(book.to_hash())

'''DELETE: delete book with id = book_id'''
@app.route('/places/<place_id>/books/<book_id>', methods = ['DELETE'])
def delete_book_by_id(place_id, book_id):
    try:
        books = Book.select().where(Book.id == int(book_id))
        book = None
        for u in books:
            book = u
        if book == None:
            return "Failed"
        book.delete_instance()
    except:
        return "Failed"
    return "success"
