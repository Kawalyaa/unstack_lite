from app.tests. base_test import BaseTest
from app.database import questions_db


class TestQuestion(BaseTest):

    def tearDown(self):
        questions_db.clear()

    def test_post_question(self):
        res = self.post_question()
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.json["message"], "created")

    def test_post_question_that_exists(self):
        self.post_question()
        res = self.post_question()
        self.assertEqual(res.status_code, 409)
        self.assertEqual(res.json["message"], "question exists")

    def test_post_empty_fields(self):
        res = self.post_empty()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json["message"], "The title , description or created_by fields should not be empty")

    def test_post_none_string_value(self):
        res = self.post_num()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json["message"], "The title, description or created_by should be a string")

    def test_get_all_questions(self):
        self.post_question()
        res = self.get_all()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["message"], "ok")

    def test_get_from_empty_db(self):
        res = self.get_all()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["message"], "The database is empty")

    def test_get_one_question(self):
        self.post_question()
        res = self.get_one()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json['message'], "ok")

    def test_get_one_missing_question(self):
        res = self.get_one()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json['message'], "question with id 1 is not found")

    def test_editing_question(self):
        self.post_question()
        res = self.edit_one()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["message"], "Question updated")

    def test_editing_missing_question(self):
        res = self.edit_one()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json["message"], "The question with id 1 is not found")

    def test_telete_question(self):
        self.post_question()
        res = self.delete_one()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["description"], "question with id 1 is deleted")
        self.assertTrue(res.json["message"])

    def test_telete_missing_question(self):
        res = self.delete_one()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json["message"], "The question with id 1 is not found")
        self.assertTrue(res.json["message"])
