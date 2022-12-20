from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository

booking_blueprint = Blueprint('bookings',__name__)

# controller uses the functions that speaks to the database via sql. when you go to the top home page of the function  
# function is executed. it then retrives information from the function in repository. 

@booking_blueprint.route("/home")
def home():
    return render_template("home/index.html")

@booking_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings = bookings)

@booking_blueprint.route("/bookings", methods = ["GET"])
def select_bookings():
    members = member_repository.select_all()
    lessons = lesson_repository.select_all()
    return render_template('bookings/index.html', lessons = lessons, members =  members)

@booking_blueprint.route("/bookings",  methods =['POST'])
def book_lesson():
    member_id = request.form['member_id']
    lesson_id = request.form['lesson_id']
    member = member_repository.select(member_id)
    lesson = lesson_repository.select(lesson_id)
    booking = Booking(member, lesson)
    booking_repository.save(booking)
    return render_template("bookings/index.html")
