from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__)
Bootstrap(app)
GoogleMaps(app, key="AIzaSyB4tGK7l8s4VDOOXz1bZYw2Roj48n-ZQm8")

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about1')
def about1():
  return render_template('about1.html')

@app.route('/about2')
def about2():
  return render_template('about2.html')

@app.route('/about3')
def about3():
  return render_template('about3.html')

@app.route('/menu1')
def menu1():
  return render_template('menu1.html')

@app.route('/menu2')
def menu2():
  return render_template('menu2.html')

@app.route('/menu3')
def menu3():
  return render_template('menu3.html')

@app.route('/gallery')
def gallery():
  return render_template('gallery.html')

@app.route('/navigation')
def navigation():
  mymap = Map(
    identifier="view_side",
    lat=37.5493705,
    lng=126.90374565,
    zoom=16,
    style="height:300px;width:device-width;margin:0;",
    markers=[(37.5493705, 126.90374565)]
  )
  return render_template('navigation.html', mymap=mymap)

if __name__ == '__main__':
  app.run(debug=True)
