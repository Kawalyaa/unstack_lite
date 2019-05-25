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
            "created_by": "Kawalya"
        }
        self.answer = {
            "description": "Yes model Y is an SUV and is out",
            "answered_by": "Kelly"
        }
        self.answer_ed = {
            "description": "Yes model Y is an SUV from Tesla",
            "answered_by": "Kelly"
        }
        self.vote = {
            "votes": 1
        }
        self.vote2 = {
            "votes": 2
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

    def edit_ans(self):
        res = self.client.put(path="api/v1/answer/id/1/owner/Kelly", data=json.dumps(self.answer_ed), content_type="application/json")
        return res

    def edit_wrong(self):
        res = self.client.put(path="/api/v1/answer/id/2/owner/Kellyi", data=json.dumps(self.answer_ed), content_type="application/json")
        return res

    def user_preffer(self):
        res = self.client.put(path="/api/v1/answer/id/1/question/1/owner/Kawalya", content_type="application/json")
        return res

    def wrong_preffer(self):
        res = self.client.put(path="/api/v1/answer/id/1/question/2/owner/Kawalyai", content_type="application/json")
        return res

    def voter(self):
        res = self.client.put(path="/api/v1/vote/answer/1", data=json.dumps(self.vote), content_type="application/json")
        return res

    def wrong_voter(self):
        res = self.client.put(path="/api/v1/vote/answer/1", data=json.dumps(self.vote2), content_type="application/json")
        return res


if __name__ == '__main__':
    unittest.main()
