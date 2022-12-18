from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.lesson import Lesson
import repositories.lesson_repository as lesson_repository
import repositories.member_repository as member_repositoy

lesson_blueprint = Blueprint('lesson', __name__)

@lesson_blueprint.route("/lessons")
def lessons():
    lessons = lesson_repository.select_all()
    return render_template("lessons/index.html", lessons = lessons)

@lesson_blueprint.route("/lessons", methods = ['POST'])
def add_lesson():
    new_name = request.form["name"]
    new_time = request.form["time"]
    new_date = request.form["date"]
    new_lesson = Lesson(new_name, new_time, new_date)
    lesson_repository.save(new_lesson)
    return redirect("/lessons")
