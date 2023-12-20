from flask_cors import CORS
from flask import Flask, request

from dynamodb import (
    add_all_courses,
    get_all_courses_info,
    add_user_rating,
)

app = Flask("JHC Workshop")
CORS(app)


@app.route("/health")
def health():
    return "<h1>Welcome to Java Home Cloud!</h1>"


@app.route("/courses")
def get_all_courses():
    return get_all_courses_info()


@app.route("/courses/<course_id>", methods=["PATCH"])
def update_user_rating(course_id):
    user_rating = request.json.get("userRating", None)

    if user_rating and user_rating in ["like", "dislike"]:
        return add_user_rating(course_id, user_rating)

    else:
        return {
            "message": "Error",
        }


if __name__ == "__main__":
    add_all_courses()

    app.run(
        debug=True,
        host="0.0.0.0",
        port=8080,
    )
