from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym import Gym
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository

member_blueprint = Blueprint('member',__name__)

@member_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)
