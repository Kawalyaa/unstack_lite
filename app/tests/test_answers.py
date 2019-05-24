from app.tests.base_test import BaseTest
from app.database import answers_db, questions_db


class TestAnswers(BaseTest):
    "class to handle answer tests"
    def tearDown(self):
        answers_db.clear()
        questions_db.clear()

    def test_post_answer(self):
        self.post_question()
        res = self.post_answer()
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.json["message"], "answered")

    def test_post_answer_to_missing_question(self):
        res = self.post_answer()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json["message"], "question id is not found")
