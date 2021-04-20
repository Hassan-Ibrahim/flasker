from flask import Flask, render_template

#Create a Flask Instance

app = Flask(__name__)

#Create a Route
@app.route('/')


#safe
#striptags
#trim
#capitalize
#upper
#lower

#def index():
#	return "<h1>Hello World...</h1>"

def index():
	first_name = 'john'
	stuff = 'This is a <strong> Bold </strong> tag.'
	favourite_pizza = ['Margharita', 'Mushroom', 'Cheese', 'Pepperoni', 20]
	return render_template('index.html', first_name=first_name, stuff=stuff,favourite_pizza=favourite_pizza )

@app.route('/user/<name>')

def user(name):
	return render_template('user.html', user_name=name)


@app.errorhandler(404)
def page_not_found(e):
	return render_template('400.html'), 404

@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500