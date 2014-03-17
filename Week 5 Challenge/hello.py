from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
  return "Hello Devon Tivona - Rapid Prototyping 2014!"

@app.route('/find')
def find():
  lookup = { 'CSCI1300' : 'ATLAS 100', 'CSCI2240' : "ITLL 1B50"}
  course = request.args.get('course')
  if course in lookup:
    room = lookup[course]
    return 'Find the classroom for ' + course + "...  " + room + "."
  else:
    return 'Sorry, no result for ' + course + "."

@app.route('/notification')
def notification():
  return 'Get notification. To be implemented.'

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
  app.run(debug=True)