What is a Web Framework:
A web framework is a collection of libraries, tools, and patterns that provide a structured way to build web applications. It simplifies common tasks such as routing, request handling, and data manipulation, allowing developers to focus on building the application's features rather than reinventing the wheel.
How to build a web framework with Flask:
Flask is itself a web framework, so you don't typically build a web framework with Flask. Instead, you use Flask to build web applications. You start by installing Flask (pip install Flask) and then create a Python script to define your application.Example:
python
Copy code
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
How to define routes in Flask:
Routes in Flask are URL patterns associated with specific functions, known as view functions, that handle requests to those URLs. You define routes using the @app.route() decorator.Example:
python
Copy code
@app.route('/')
def index():
    return 'This is the homepage'

@app.route('/about')
def about():
    return 'About page'
What is a route:
A route in web development defines a URL pattern and specifies what should happen when a client makes a request to that URL.
How to handle variables in a route:
You can include variable parts in a route URL by enclosing them in < >. These variables are passed to the view function as arguments.Example:
python
Copy code
@app.route('/user/<username>')
def profile(username):
    return f'User profile: {username}'
What is a template:
A template is an HTML file with placeholders for dynamic content. It allows you to separate the structure of your web pages from the Python code that generates them, making it easier to manage and maintain your code.
How to create a HTML response in Flask by using a template:
Flask uses the Jinja2 templating engine to render HTML templates. You can render a template using the render_template() function and pass data to the template as arguments.Example:
python
Copy code
from flask import render_template

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
How to create a dynamic template (loops, conditions…):
Jinja2 templates support various features such as loops, conditions, filters, and template inheritance, allowing you to create dynamic and reusable HTML templates.Example (hello.html):
html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello</title>
</head>
<body>
    {% if name %}
        <h1>Hello, {{ name }}!</h1>
    {% else %}
        <h1>Hello, World!</h1>
    {% endif %}
</body>
</html>
How to display in HTML data from a MySQL database:
You can use Flask-SQLAlchemy or other database libraries to interact with a MySQL database in Flask. After fetching data from the database, you pass it to the template for rendering.Example:
python
Copy code
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)
Example (index.html):
html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User List</title>
</head>
<body>
    <h1>User List</h1>
    <ul>
        {% for user in users %}
            <li>{{ user.username }}</li>
        {% endfor %}
    </ul>
</body>
</html>