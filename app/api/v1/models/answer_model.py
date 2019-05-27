import datetime
import time
from flask import request
from app.database import answers_db, questions_db
my_db = questions_db
second_db = answers_db


class AnswerModel:
    def __init__(self, description="description", answered_by="answered_by", user_preffered=False, votes=0):
        self.answer_id = len(second_db) + 1
        self.description = description
        self.answered_by = answered_by
        self.answered_on = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        self.user_preffered = user_preffered
        self.votes = votes
        self.second_db = second_db

    def save_answer(self, question_id):
        answer = {
            "answer_id": self.answer_id,
            "question_id": question_id,
            "description": self.description,
            "answered_by": self.answered_by,
            "answered_on": self.answered_on,
            "user_preffered": self.user_preffered,
            "votes": self.votes
        }
        self.second_db.append(answer)
        return self.second_db

    def edit_ans(self, answer_id, answered_by):
        req = request.get_json()
        for answer in self.second_db:
            if answer["answer_id"] == answer_id and answer["answered_by"] == answered_by:
                answer["description"] = req["description"]
                answer["answered_by"] = req["answered_by"]
                return answer

    def make_ans_user_preffered(self, answer_id, question_id):
        for answer in self.second_db:
            if answer["answer_id"] == answer_id and answer["question_id"] == question_id:
                answer["user_preffered"] = True
                return answer

    def vote(self, answer_id):
        req = request.get_json()
        for answer in self.second_db:
            if answer["answer_id"] == answer_id:
                reque = req["votes"]
                if reque not in [1, -1]:
                    return "bad vote"
                answer["votes"] += reque
                return answer

    def delete_qtn_and_ans(self, question_id):
        for answer in self.second_db:
            if answer["question_id"] == question_id:
                self.second_db.remove(answer)
                return "answer deleted"
