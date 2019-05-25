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

    def test_edit_answer_by_owner(self):
        self.post_question()
        self.post_answer()
        res = self.edit_ans()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["message"], "answer with id 1 has been edited")

    def test_edit_answer_with_wrong_id_or_name(self):
        self.post_question()
        self.post_answer()
        res = self.edit_wrong()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json["message"], "The answer id 2 or the owner Kellyi is not found")

    def test_set_user_preffered_by_question_owner(self):
        self.post_question()
        self.post_answer()
        res = self.user_preffer()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["message"], "User preffered set")

    def test_set_user_preffered_not_by_question_owner(self):
        self.post_question()
        self.post_answer()
        res = self.wrong_preffer()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json["message"], "Not allowed! only question owner should set user_preffered")

    def test_vote_for_answer(self):
        self.post_question()
        self.post_answer()
        res = self.voter()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["message"], "Answer voted successful")

    def test_vote_for_answer_with_wrong_votes(self):
        self.post_question()
        self.post_answer()
        res = self.wrong_voter()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json["message"], "invalid voting, vote should be either (1 or -1)")

    def test_get_question_and_answer(self):
        self.post_question()
        self.post_answer()
        res = self.get_qtn_and_ans()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["message"], "ok")

    def test_get_missing_question_and_answer(self):
        self.post_question()
        self.post_answer()
        res = self.get_missing_qtn_and_ans()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json["message"], "The question and answer with question id 2 is not found")

    def test_delete_question_and_answer(self):
        self.post_question()
        self.post_answer()
        res = self.delete_qtn_and_ans()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json["description"], "The question and answer with question_id 1 is deleted")

    def test_delete_missing_question_and_answer(self):
        self.post_question()
        self.post_answer()
        res = self.delete_missing_qtn_and_ans()
        self.assertEqual(res.status_code, 404)
