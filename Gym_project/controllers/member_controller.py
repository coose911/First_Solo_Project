from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository

member_blueprint = Blueprint('members',__name__)

# controller uses the functions that speaks to the database via sql. when you go to the top home page of the function  
# function is executed. it then retrives information from the function in repository. 

@member_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

@member_blueprint.route("/members", methods = ["POST"])
def add_member():
    new_first_name = request.form["first_name"]
    new_last_name = request.form["last_name"]
    new_dob = request.form["dob"]
    new_member = Member(new_first_name, new_last_name, new_dob)
    member_repository.save(new_member)
    return redirect("/members")

@member_blueprint.route("/members/<int:id>/update", methods = ["GET"])
def edit(id):
    member = member_repository.select(id)
    return render_template("/members/update.html", member =  member)


@member_blueprint.route("/members/<id>", methods = ["POST"])
def update_member(id):
    new_name = request.form["first_name"]
    new_second_name = request.form["last_name"]
    new_dob = request.form["dob"]
    updated_details = Member(new_name, new_second_name, new_dob, int(id))
    member_repository.update(updated_details)
    return redirect("/members")
