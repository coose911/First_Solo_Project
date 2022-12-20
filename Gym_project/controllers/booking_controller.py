from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository

booking_blueprint = Blueprint('booking',__name__)

@booking_blueprint.route("/home")
def home():
    return render_template("home/index.html")

