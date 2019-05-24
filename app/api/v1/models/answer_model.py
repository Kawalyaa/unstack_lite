import datetime
import time
from app.database import answers_db, questions_db
my_db = questions_db
second_db = answers_db


class AnswerModel:
    def __init__(self, description, answered_by):
        self.answer_id = len(second_db) + 1
        self.description = description
        self.answered_by = answered_by
        self.answered_on = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        self.second_db = second_db

    def save_answer(self, question_id):
        answer = {
            "answer_id": self.answer_id,
            "question_id": question_id,
            "description": self.description,
            "answered_by": self.answered_by,
            "answered_on": self.answered_on
        }
        self.second_db.append(answer)
        return self.second_db

    def check_answer(self, my_answer):
        for answer in second_db:
            if answer["description"] == my_answer:
                return "answer exists"
