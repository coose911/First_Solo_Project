from flask import Flask, render_template

from controllers.booking_controller import booking_blueprint
from controllers.member_controller import member_blueprint
from controllers.lesson_controller import lesson_blueprint
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository

app = Flask(__name__)


app.register_blueprint(booking_blueprint)
app.register_blueprint(member_blueprint)
app.register_blueprint(lesson_blueprint)

# decorator which defines the home page as / and links the index.html file
@app.route('/')
def home():
    members = member_repository.select_all()
    lessons = lesson_repository.select_all()
    return render_template('index.html', lessons = lessons, members = members)

# @app.route('/')
# def select_bookings():
#     members = member_repository.select_all()
#     lessons = lesson_repository.select_all()
#     return render_template('index.html', lessons = lessons, members =  members)


if __name__ == '__main__':
    app.run(debug=True)
