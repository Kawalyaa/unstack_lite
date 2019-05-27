from flask import Blueprint, jsonify, make_response, request
from app.api.v1.models.answer_model import AnswerModel
from app.api.v1.models.question_model import QuestionModel
from app.api.v1.models.answer_model import second_db
from app.api.v1.models.question_model import my_db

answer = Blueprint('answer', __name__, url_prefix='/api/v1')


@answer.route("/answers/<int:question_id>", methods=['POST'])
def post_answer(question_id):
    """endpoint for posting answer"""
    qtn_id = [answer for answer in my_db if answer["question_id"] == question_id]
    if not qtn_id:
        return jsonify({"message": "question id is not found"}), 404
    req = request.get_json()
    description = req["description"]
    answered_by = req["answered_by"]

    ans_detail = {
        "description": description,
        "answered_by": answered_by
    }
    # validate input
    if not ans_detail["description"] or not ans_detail["answered_by"]:
        return jsonify({"message": "description and answered_by are required fields"}), 404
    elif isinstance(ans_detail["answered_by"], int):
        return jsonify({"message": "answered_by should be a string"}), 404

    detail = AnswerModel(**ans_detail)
    # check if answer exists
    chec = [answer for answer in second_db if answer["description"] == ans_detail["description"]]
    if chec:
        return jsonify({"message": "answer exists"}), 409
    # save answer
    ans = detail.save_answer(question_id)
    return make_response(jsonify({
        "message": "answered",
        "answer": ans
    }), 201)


@answer.route('/answer/id/<int:answer_id>/owner/<answered_by>', methods=['PUT'])
def edit_answer(answer_id, answered_by):
    """endpoint for editing the answer by answer owner"""
    update = AnswerModel().edit_ans(answer_id, answered_by)
    if update:
        message = "answer with id {} has been edited".format(answer_id)
        return make_response(jsonify({
            "message": message,
            "answer": update
        }), 200)
    msg = "The answer id {} or the owner {} is not found".format(answer_id, answered_by)
    return jsonify({"message": msg}), 404


@answer.route('/answer/id/<int:answer_id>/question/<int:question_id>/owner/<created_by>', methods=['PUT'])
def set_user_preffered(answer_id, question_id, created_by):
    """method to handle make answer user preffered by question owner"""
    # make answer of given question user_preffered
    ans = AnswerModel().make_ans_user_preffered(answer_id, question_id)
    # check if question and owner exists
    qtn_owner = QuestionModel().check_name(question_id, created_by)
    if ans and qtn_owner:
        return make_response(jsonify({
            "message": "User preffered set",
            "user_preffered": ans
        }), 200)
    message = "Not allowed! only question owner should set user_preffered"
    return jsonify({"message": message}), 404


@answer.route("/vote/answer/<int:answer_id>", methods=['PUT'])
def vote_answer(answer_id):
    """endpoint for voting the answer"""
    voter = AnswerModel().vote(answer_id)
    if voter:
        return make_response(jsonify({
            "message": "Answer voted successful",
            "answer": voter
        }), 200)

    return jsonify({"message": "invalid voting, vote should be either (1 or -1)"}), 400


@answer.route("/question/answer/<int:question_id>", methods=['GET'])
def get_question_and_answer(question_id):
    """endpoint for geting question and answer"""
    ans = [y for y in second_db if y["question_id"] == question_id]
    qtn = QuestionModel().get_one_qtn(question_id)
    if ans and qtn:
        return make_response(jsonify({
            "message": "ok",
            "question": qtn,
            "answer": ans
        }), 200)
    message = "The question and answer with question id {} is not found".format(question_id)
    return jsonify({"message": message}), 404


@answer.route("/delete/question/answer/<int:question_id>", methods=['DELETE'])
def delete_question_and_answer(question_id):
    """endpoint for deleting question and answer"""
    qtn = QuestionModel().delete(question_id)
    ans = AnswerModel().delete_qtn_and_ans(question_id)
    if qtn and ans:
        message = "The question and answer with question_id {} is deleted".format(question_id)
        return make_response(jsonify({
            "message": "ok",
            "description": message
        }), 200)
    return jsonify({"message": "The answer and question with question id {} is not found".format(question_id)}), 404
