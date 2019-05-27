from flask import request, jsonify, make_response, Blueprint
from app.api.v1.models.question_model import my_db
from app.api.v1.models.question_model import QuestionModel


question = Blueprint('question', __name__, url_prefix='/api/v1')


@question.route('/questions', methods=['POST'])
def post_question():
    """endpoint for posting a question"""
    req = request.get_json()
    title = req['title']
    description = req['description']
    created_by = req['created_by']
    qtn = {
        "title": title,
        "description": description,
        "created_by": created_by
    }
    if not qtn["title"] or not qtn["description"] or not qtn["created_by"]:
        return jsonify({"message": "The title , description or created_by fields should not be empty"}), 400

    if isinstance(qtn["title"], int)or isinstance(qtn["description"], int) or isinstance(qtn["created_by"], int):
        # it should not be an integer
        return jsonify({"message": "The title, description or created_by should be a string"}), 400
    # load the values as a dict
    ques = QuestionModel(**qtn)
    # check if question exists
    if ques.check_exist(qtn["description"]) == "The question exists":
        return jsonify({"message": "question exists"}), 409
    # save the question
    res = ques.save_question()
    return make_response(jsonify({
        "message": "created",
        "question": res
    }), 201)


@question.route("/questions", methods=['GET'])
def get_all_quetions():
    """endpoint for geting all questions from database"""
    data = QuestionModel()
    res = data.get_all_qtn()
    if len(res) is 0:
        return jsonify({
            "message": "The database is empty",
            "database": res
        }), 200

    return make_response(jsonify({
        "message": "ok",
        "questions": res
    }), 200)


@question.route("/questions/one/<int:question_id>", methods=['GET'])
def geta_one_question(question_id):
    """endpoint for geting one question"""
    data = [question for question in my_db if question["question_id"] == question_id]
    if not data:
        message = "question with id {} is not found".format(question_id)
        return jsonify({"message": message}), 404
    return make_response(jsonify({
        "message": "ok",
        "question": data
    }), 200)


@question.route("/questions/edit/<int:question_id>", methods=['PUT'])
def update_question(question_id):
    """endpoint for editing a question"""
    new = QuestionModel().edit_qtn(question_id)
    if new:
        return make_response(jsonify({
            "message": "Question updated",
            "question": new
        }), 200)
    message = "The question with id {} is not found".format(question_id)
    return jsonify({"message": message}), 404


@question.route("/questions/delete/<int:question_id>", methods=['DELETE'])
def delete_question(question_id):
    """endpoint for deleting aquestion"""
    # deleted = QuestionModel().delete(question_id)
    deleted = [x for x in my_db if x["question_id"] == question_id]
    msg = "question with id {} is deleted".format(question_id)
    if deleted:
        return make_response(jsonify({
            "message": "ok",
            "description": msg
        }), 200)
    message = "The question with id {} is not found".format(question_id)
    return jsonify({"message": message}), 404
