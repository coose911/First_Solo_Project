from flask import Flask, render_template

from controllers.booking_controller import booking_blueprint
from controllers.member_controller import member_blueprint
from controllers.lesson_controller import lesson_blueprint
import repositories.booking_repository as booking_repository

app = Flask(__name__)


app.register_blueprint(booking_blueprint)
app.register_blueprint(member_blueprint)
app.register_blueprint(lesson_blueprint)

# decorator which defines the home page as / and links the index.html file
@app.route('/')
def home():
    bookings = booking_repository.select_all()
    return render_template('index.html', bookings = bookings)


if __name__ == '__main__':
    app.run(debug=True)
