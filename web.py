from bottle import route, run
from bottle import template
from bottle import get, post, request
from bottle import static_file
from bottle import error


@route('/hello')
def hello():
	return "Hello!"

@route('/')

@route('/index')
def index():
	return "This is another page"

@route('/hello/<name>')
def greet(name='Stranger'):
	return template('Hello {{name}}, how are you?', name=name)

@route('/wiki/<pagename>')
def show_wiki_page(pagename):
	return template('This is the {{pagename}} page!', pagename=pagename)

@route('/action/<user>')
def user_api(action, user):
	if action and user:
		return template('Hello {{user}}!', user=user)
	else:
		return template('Sorry, an error occurred')

# filters can be used to define more specific parameter wildcards, and/or
# to transform the covered part of the URL before it is passed to the callback.
# :int matches digits only and converts the value to an integer
# :float is similar to :int, but for decimal numbers
@route('/object/<id:int>')
def callback(id):
	assert isinstance(id, int)

# :re allows you to specify a custom regular expression in the config field.
@route('/show/<name:re:[a-z]+>')
def callback(name):
	assert name.isalpha()

# :path matches all characters including the slash character, and can be used
# to match more than one path segment
@route('/static/<path:path>')
def callback(path):
	return static_file(path, ...)

# Http request methods
@get('/login') # or @route('/login')
def login():
	return '''
		<form action="/login" method="post">
			Username: <input name="username" type="text" />
			Password: <input name="password" type="password" />
			<input value="Login" type="submit" />
		</form>
	'''
@post('/login') # or @route('/login', method='POST')
def do_login():
	username = request.forms.get('username')
	password = request.forms.get('password')
	if check_login(username, password):
		return "<p>Your login information was correct.</p>"
	else:
		return "<p>Login failed. Try entering your username and password again.</p>"


# Special HTTP request methods:
	# HEAD - used to ask for the response identical to the one that would correspond to
	# a GET request, but without the response body (useful for retrieving meta-information
	# about a resource without having to download the entire document). Bottle handles
	# these requests automatically by deferring to the GET route and cutting off the 
	# request body, if present.

	# ANY - used to match requests regardless of their HTTP method, but only if
	# no other more specific route is defined. This is helpful for proxy-routes
	# that redirect requests to more specific sub-applications.

	# Summary of special HTTP requests:
	# HEAD requests fall back to GET routes
	# All requests fall back to ANY routes, but only if there is no matching route
	# for the original request method.


# Routing static files:

# @route('/static/<filename>')
# def server_static(filename):
# 	return static_file(filepath, root='/path/to/static/file')

# Create a custom error message:
@error(404)
def error404(error):
	return 'Nothing here, sorry'

# the run() call starts a built-in development server
# debug should be switched to False for public applications
run(host='localhost', port=8080, debug=True)