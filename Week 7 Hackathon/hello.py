from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Pet(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=False)
  trait = db.Column(db.String(80), unique=False)
  color = db.Column(db.String(80), unique=False)
  image = db.Column(db.String(120), unique=False)

  def __init__(self, name, trait, color, image):
    self.name = name
    self.trait = trait
    self.color = color
    self.image = image

  def __repr__(self):
    return self.name

@app.route('/search')
def search():
  color = request.args.get('color')
  trait = request.args.get('trait')
  pets = None
  if (color and trait):
    pets = Pet.query.filter_by(color=color.title(), trait=trait.title())
  elif color:
    pets = Pet.query.filter_by(color=color.title())
  elif trait:
    pets = Pet.query.filter_by(trait=trait.title())
  else:
    pets = Pet.query.all()
  # for pet in pets:
  #   trait = pet.trait
  #   pet.trait = pet.color
  #   pet.color = trait
  # db.session.commit()
  return render_template('index.html', pets=pets)

@app.route('/view/<name>')
def view(name=None):
  pet = Pet.query.filter_by(name=name).first()
  return render_template('view.html', pet=pet)

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

