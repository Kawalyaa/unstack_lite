import datetime
import time
from flask import request
from app.database import questions_db

my_db = questions_db


class QuestionModel:
    def __init__(self, title="title", description="description", created_by="created_by"):
        self.title = title
        self.description = description
        self.created_by = created_by
        self.created_on = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        self.db = my_db

    def save_question(self):
        question = {
            "question_id": len(self.db) + 1,
            "title": self.title,
            "description": self.description,
            "created_on": self.created_on,
            "created_by": self.created_by
        }
        self.db.append(question)
        return self.db

    def check_exist(self, item):
        for aqtn in self.db:
            if aqtn["description"] == item:
                return "The question exists"

    def get_all_qtn(self):
        return self.db

    def get_one_qtn(self, question_id):
        # search for question_id in db
        for question in self.db:
            if question["question_id"] == question_id:
                return question

    def edit_qtn(self, question_id):
        req = request.get_json()
        # search for question_id in db
        for question in self.db:
            if question["question_id"] == question_id:
                question["title"] = req["title"]
                question["description"] = req["description"]
                question["created_by"] = req["created_by"]
                return question

    def delete(self, question_id):
        # search for question_id in db
        for question in self.db:
            if question["question_id"] == question_id:
                self.db.remove(question)
                return "question with id {} is deleted".format(question_id)

    def check_name(self, question_id, created_by):
        for question in self.db:
            if question["created_by"] == created_by and question["question_id"] == question_id:
                return "The id  and name exists"
