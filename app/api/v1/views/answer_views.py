from flask import Blueprint, jsonify, make_response, request
from app.api.v1.models.answer_model import AnswerModel
from app.api.v1.models.question_model import QuestionModel

answer = Blueprint('answer', __name__, url_prefix='/api/v1')


@answer.route("/answers/<int:question_id>", methods=['POST'])
def post_answer(question_id):
    qtn_id = QuestionModel().get_qtn_by_id(question_id)
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
    if detail.check_answer(ans_detail["description"]):
        return jsonify({"message": "answer exists"}), 409
    # save answer
    ans = detail.save_answer(question_id)
    return make_response(jsonify({
        "message": "answered",
        "answer": ans
    }), 201)
