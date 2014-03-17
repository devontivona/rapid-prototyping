from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)

  def __init__(self, username, email):
    self.username = username
    self.email = email

  def __repr__(self):
    return "User:{0} Email:{1}".format(self.username, self.email)

@app.route('/users')
def users():
  return str(User.query.all())

@app.route('/users_template')
def users_template():
  return render_template('users.html', users=User.query.all())

if __name__ == "__main__":
  app.run(debug=True)

# from flask import Flask
# from flask import request
# app = Flask(__name__)

# @app.route('/')
# def index():
#   return "Hello Devon Tivona - Rapid Prototyping 2014!"

# # @app.route('/find')
# # def find():
# #   lookup = { 'CSCI1300' : 'ATLAS 100', 'CSCI2240' : "ITLL 1B50"}
# #   course = request.args.get('course')
# #   if course in lookup:
# #     room = lookup[course]
# #     return 'Find the classroom for ' + course + "...  " + room + "."
# #   else:
# #     return 'Sorry, no result for ' + course + "."

# # @app.route('/notification')
# # def notification():
# #   return 'Get notification. To be implemented.'



# # @app.route('/hello/')
# # @app.route('/hello/<name>')
# # def hello(name=None):
# #     return render_template('hello.html', name=name)

# @app.route('/home')
# def home():
#     return render_template('home.html')
