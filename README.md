[![Build Status](https://travis-ci.org/Kawalyaa/unstack.svg?branch=development_perfect)](https://travis-ci.org/Kawalyaa/unstack)  [![Coverage Status](https://coveralls.io/repos/github/Kawalyaa/unstack/badge.svg?branch=feature)](https://coveralls.io/github/Kawalyaa/unstack?branch=feature)  [![Maintainability](https://api.codeclimate.com/v1/badges/2bfcb5ec433449bbc047/maintainability)](https://codeclimate.com/github/Kawalyaa/unstack/maintainability)

# UNSTACK_LITE

Unstack_lite is a platform which enables people to ask question and get answers



## Built with

* python 3
* flask

## Features

  1. User can post questions
  1. user can delete questions they post
  1. User can post answers
  1. Users can view answers to the questions
  1. Question owner can make answer user user_preferred
  1. Answer owner can edit answers
  1. User can delete question with its answers
  1. User can vote answers

## Installing

Step 1

### Clone this repository

```
$ git clone https://github.com/Kawalyaa/ustack_lite.git

$ cd unstack

```

Create and activate the virtual environment

```
$ python3 -m venv venv

$ source venv/bin/activate

```

Install project dependencies

```
pip install -r requirements.txt

```

Step 2

### Setup Databases

Use data structres as databases eg lists

Main Database

```
questions_db = []

answers_db = []
```

Step 3

### Storing the environmental variables

```
export FLASK_APP="run.py"
export FLASK_ENV="development"
```

step 4

### Running the application

```
$ flask run
```

Step 5

### Testing the application

```
$ nosetests -v app/tests
```

## API-ENDPOINTS

 Method | Endpoints | Functionality
 ------ | --------- | -------------
 |      |         Questions endpoints       |
 POST | /api/v1/questions | A user can post question
 GET | /api/v1/questions | A user can view all the questions
 GET | /api/v1/questions/one/<int:question_id> | A user can view a single question
 PUT | /api/v1//questions/edit/<int:question_id> | A user can edit a question
 DELETE | api/v1/questions/delete/<int:question_id> | A user can delete a question
 |      |             Answers Endpoint                    |
 POST | /api/v1/answers/<int:question_id> | A user can post Answers
 PUT | /api/v1/answer/id/<int:answer_id>/owner/<answered_by> | A user can edit strictly the answer owner
 PUT | /api/v1/answer/id/<int:answer_id>/question/<int:question_id>/owner/<created_by> | A question owner can make answer user preffered
 PUT | /api/v1/vote/answer/<int:answer_id> | A user can vote for answer
 GET | /api/v1/question/answer/<int:question_id> | A user can get question with answer
 DELETE | /api/v1/delete/question/answer/<int:question_id> | A user can delete a question and its answer

## Author

*[KAWALYA ANDREW](https://github.com/Kawalyaa)*
