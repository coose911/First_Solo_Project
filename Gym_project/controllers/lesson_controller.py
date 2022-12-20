from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.lesson import Lesson
import repositories.lesson_repository as lesson_repository
import repositories.member_repository as member_repositoy

lesson_blueprint = Blueprint('lessons', __name__)

# controller uses the functions that speaks to the database via sql. when you go to the top home page of the function  
# function is executed. it then retrives information from the function in repository. 

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

@lesson_blueprint.route("/lessons/<int:id>/update", methods = ["GET"])
def edit(id):
    lesson = lesson_repository.select(id)
    return render_template("lessons/update.html", lesson = lesson)

@lesson_blueprint.route("/lessons/<int:id>", methods = ["POST"])
def update_lesson(id):
    new_lesson = request.form["name"]
    new_time = request.form["time"]
    new_date = request.form["date"]
    updated_lesson = Lesson(new_lesson, new_time, new_date, int(id))
    lesson_repository.update(updated_lesson)
    return redirect("/lessons")