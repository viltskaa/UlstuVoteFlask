from flask import Blueprint, request, current_app, json

from database.models import Teacher
from repositories import TeacherRepository

teacher_blueprint = Blueprint('teacher', __name__)


@teacher_blueprint.route("/all")
def get_teachers():
    val = TeacherRepository().get_all()
    return current_app.response_class(
        response=json.dumps(val),
        status=200,
        mimetype='application/json'
    )


@teacher_blueprint.route("/get/<int:tid>")
def get_teacher(tid):
    teacher = TeacherRepository().get_by_id(tid)
    if teacher:
        return current_app.response_class(
            response=json.dumps(teacher.to_dict()),
            status=200,
            mimetype='application/json'
        )
    return current_app.response_class(
        response="not found",
        status=500,
        mimetype='application/json'
    )


@teacher_blueprint.route('/add')
def add_teacher():
    args = request.args
    email = args.get("email", type=str, default="")
    classroom = args.get("classroom", type=str, default="")
    fio = args.get("fio", type=str, default="")
    password = args.get("password", type=str, default="")
    school = args.get("school", type=str, default="")
    image = args.get("image", type=str, default="")

    teacher = TeacherRepository().add(
        Teacher(
            None,
            email,
            classroom,
            fio,
            password,
            school,
            image
        )
    )

    if teacher:
        return current_app.response_class(
            response=json.dumps(teacher.to_dict()),
            status=200,
            mimetype='application/json'
        )
    return current_app.response_class(
        response=None,
        status=500,
        mimetype='application/json'
    )
