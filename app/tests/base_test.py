import json
import unittest
from app import create_app


class BaseTest(unittest.TestCase):
    """base class for testing """
    def setUp(self):
        """This method is used to construct all our tests"""
        app = create_app("testing")
        app.testing = True
        self.client = app.test_client()

        self.qtn = {
            "title": "TECH",
            "description": "is Tesla model y out?",
            "created_by": "Kawalya"
        }

        self.empty = {
            "title": "",
            "description": "",
            "created_by": ""
        }
        self.num = {
            "title": 1,
            "description": 2,
            "created_by": 3
        }
        self.update = {
            "title": "TECHNOLOGY",
            "description": "is Tesla model y an SUV?",
            "created_by": "Kawalyaa"
        }
        self.answer = {
            "description": "Yes model Y is an SUV",
            "answered_by": "Kelly"
        }

    def tearDown(self):
        pass

    def post_question(self):
        res = self.client.post(path="/api/v1/questions", data=json.dumps(self.qtn), content_type="application/json")
        return res

    def post_empty(self):
        res = self.client.post(path="/api/v1/questions", data=json.dumps(self.empty), content_type="application/json")
        return res

    def post_num(self):
        res = self.client.post(path="/api/v1/questions", data=json.dumps(self.num), content_type="application/json")
        return res

    def get_all(self):
        res = self.client.get(path="/api/v1/questions", content_type='application/json')
        return res

    def get_one(self):
        res = self.client.get(path="/api/v1/questions/one/1", content_type='application/json')
        return res

    def edit_one(self):
        res = self.client.put(path="/api/v1/questions/edit/1", data=json.dumps(self.update), content_type='application/json')
        return res

    def delete_one(self):
        res = self.client.delete(path="/api/v1/questions/delete/1", content_type='application/json')
        return res

    def post_answer(self):
        res = self.client.post(path="/api/v1/answers/1", data=json.dumps(self.answer), content_type="application/json")
        return res


if __name__ == '__main__':
    unittest.main()
