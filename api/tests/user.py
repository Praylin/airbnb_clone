class AirbnbIndexTestCase(unittest.TestCase):
    def setUp(self):
         User.delete().execute()

    def tearDown(self):
        User.delete().execute()

    #validate if the POST request => POST /users
    def test_create(self):
        resp = requests.post('http://localhost:5555/users', data=json.dumps({"email": "test@test.test",
                                                    "password": "TeSt!2#",
                                                    "first_name": "Testy",
                                                    "last_name": "McTest",
                                                    "is_admin": False}))
        assert(resp.text=="Success")

    #validate if the GET request => GET /users
    def test_list(self):
        self.test_create()
        resp = requests.get('http://localhost:5555/users')
        data = json.loads(resp.text)
        assert(len(data)==1)

    #validate if the GET request on a user ID => GET /users/<user_id>
    def test_get(self):
        self.test_create()
        resp = requests.get('http://localhost:5555/users')
        data = json.loads(resp.text)
        user_id = data["users"][0]["id"]
        resp = requests.get('http://localhost:5555/users/' + str(user_id))
        data = json.loads(resp.text)
        assert(data["id"]==user_id)

    #validate if the DELETE request on a user ID => DELETE /users/<user_id>
    def test_delete(self):
        self.test_create()
        resp = requests.get('http://localhost:5555/users')
        data = json.loads(resp.text)
        user_id = data["users"][0]["id"]
        resp = requests.delete('http://localhost:5555/users/' + str(user_id))
        assert(resp.text=="Success")

    #validate if the PUT request on a user ID => PUT /users/<user_id>
    def test_update(self):
        self.test_create()
        resp = requests.get('http://localhost:5555/users')
        data = json.loads(resp.text)
        user_id = data["users"][0]["id"]
        resp = requests.put('http://localhost:5555/users/' + str(user_id),
            data=json.dumps({
                "first_name": "TESSSSTTTTTT",
            }))
        assert(resp.text != "Failed")
        resp = requests.get('http://localhost:5555/users/' + str(user_id))
        data = json.loads(resp.text)
        assert(data["first_name"]=="TESSSSTTTTTT")

if __name__ == '__main__':
    unittest.main()
