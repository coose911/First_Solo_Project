from flask import Flask, render_template

from controllers.gym_controller import gym_blueprint
from controllers.member_controller import member_blueprint
from controllers.lesson_controller import lesson_blueprint

app = Flask(__name__)


app.register_blueprint(gym_blueprint)
app.register_blueprint(member_blueprint)
app.register_blueprint(lesson_blueprint)

# decorator which defines the home page as / and links the index.html file
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
