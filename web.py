#!/usr/bin/env python3
import bottle
from bottle import route, run
from bottle import template
from bottle import get, post, request
from bottle import static_file
from bottle import error
from bottle_sqlite import SQLitePlugin
# import cherrypy

# Restart the server process every time
# a module file is edited.
# (Warning! This will create a child process, 
# using the same command line arguments used
# to start the main server process, which means that
# all module-level code is executed at least twice!)
run(reloader=True)

# set debug=True to deactivate template caching.


# Consider using multi-threaded server library - 
# such as cherrypy - for production:

# class HelloWorld(object):
# 	def index(self):
# 		return "Hello World!"
# 	index.exposed = True

# cherrypy.quickstart(HelloWorld())


# Install the SQLite plugin application-wide.
# SQLitePlugin is smart and will only affect
# route callbacks that need a database connection.
# install(SQLitePlugin(dbfile='/tmp/test.db'))

# Disabling plugins for specific routes with 'skip':

# sqlite_plugin = SQLitePlugin(dbfile='/tmp/test1.db')
# install(sqlite_plugin)

# dbfile1 = '/tmp/test1.db'
# dbfile2 = '/tmp/test2.db'

# The 'skip' parameter accepts a single value or a list of values.
# You can identify the plugin to be skipped by referencing a name, class, 
# or instance. Set skip=True to skip all plugins.

# @route('/open/<db>', skip=[sqlite_plugin])
# def open_db(db):
# 	# The 'db' keyword argument is not touched by the plugin.

# 	# The plugin handle can be used for runtime configuration:
# 	if db == 'test1':
# 		sqlite_plugin.dbfile = dbfile1
# 	elif db = 'test2':
# 		sqlite_plugin.dbfile = dbfile2
# 	else:
# 		abort(404, "No such database.")

# 	return "Database File switched to: " + sqlite_plugin.dbfile

# Create an application object - an instance of Bottle
# This object oriented approach supports reusability, as it
# permits the app object to be imported from this 
# module and merged with other applications using Bottle.mount()

# app = Bottle()

# with app:
# 	assert bottle is default_app()
#	@route('/')

# Routes

# @route('/hello')
# def hello():
#  	return "Hello!"

# @route('/show/<post_id:int>')
# def show(db, post_id):
# 	c = db.execute('SELECT title, content FROM posts WHERE id = ?', (post_id,))
# 	row = c.fetchone()
# 	return template('show_post', title=row['title'], text=row['content'])

# @route('/contact')
# def contact_page():
# 	'''This callback does not need a db connection. Because the 'db'
# 	keyword argument is missing, the sqlite plugin ignores this callback
# 	completely. '''
# 	return template('contact')

# @route('/index')
# def index():
# 	return "This is another page"

# @route('/hello/<name>')
# def greet(name=input("Hello, what is your name? ")):
# 	return template('Hey {{name}}!', name=name)

# @route('/wiki/<pagename>')
# def show_wiki_page(pagename):
# 	return template('This is the {{pagename}} page!', pagename=pagename)

# @route('/action/<user>')
# def user_api(action, user):
# 	if action and user:
# 		return template('Hello {{user}}!', user=user)
# 	else:
# 		return template('Sorry, an error occurred')

# filters can be used to define more specific parameter wildcards, and/or
# to transform the covered part of the URL before it is passed to the callback.
# :int matches digits only and converts the value to an integer
# :float is similar to :int, but for decimal numbers
# @route('/object/<id:int>')
# def callback(id):
# 	assert isinstance(id, int)

# :re allows you to specify a custom regular expression in the config field.
# @route('/show/<name:re:[a-z]+>')
# def callback(name):
# 	assert name.isalpha()

# :path matches all characters including the slash character, and can be used
# to match more than one path segment
# @route('/static/<path:path>')
# def callback(path):
# 	return static_file(path, ...)

# Http request methods
# @get('/login') # or @route('/login')
# def login():
# 	return '''
# 		<form action="/login" method="post">
# 			Username: <input name="username" type="text" />
# 			Password: <input name="password" type="password" />
# 			<input value="Login" type="submit" />
# 		</form>
# 	'''
# @post('/login') # or @route('/login', method='POST')
# def do_login():
# 	username = request.forms.get('username')
# 	password = request.forms.get('password')
# 	if check_login(username, password):
# 		return "<p>Your login information was correct.</p>"
# 	else:
# 		return "<p>Login failed. Try entering your username and password again.</p>"


# Other attributes for accessing form data:

# Attribute 				Get Form Fields 	POST Form fields 	File Uploads

# BaseRequest.query			yes					no 					no
# BaseRequest.forms 		no 					yes 				no
# BaseRequest.files 		no 					no 					yes
# BaseRequest.params 		yes 				yes 				no
# BaseRequest.GET 			yes 				no 					no
# BaseRequest.POST 			no 					yes 				yes


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

# HTTP errors and redirects:

# Create a custom error message:
# @error(404)
# def error404(error):
# 	return 'Nothing here, sorry'

# The abort() function - a shortcut for generating HTTP error pages:

# from bottle import route, abort
# @route('/restricted')
# def restricted():
# 	abort(401, "Access denied.")

# Redirect a client to a different URL with the 303 See Other response
# with the Location header set to the new URL.
# This can be accomplished with redirect():

# from bottle import redirect
# @route('/wrong/url')
# def wrong():
# 	redirect("/right/url") # where 'wrong' is the protected URL and 'right' is the redirect path

# Other Exceptions:

# All exceptions other than HTTPResponse or HTTPError wil result in a 500 Internal Server Error
# response. This behavior can be set to False (to handle exceptions in your middleware instead) with
# bottle.app().catchall = False

# Templates:

# To render a template, you can use the template() function or the view() decorator.
# Simply provide the name of the template and the variables you want to pass to the 
# template as keyword arguments:

# @route('/hello')
# @route('/hello/<name>')
# def hello(name='World'):
# 	return template('hello_template', name=name)

# @route('/hello')
# @route('/hello/<name>')
# @view('hello_template')
# def hello(name='World'):
# 	return dict(name=name)


# Passing a custom MIME type for static files:

# @route('/images/<filename:re:.*\.png>')
# def send_image(filename):
# 	return static_file(filename, root='/path/to/image/files', mimetype='image/png')

# @route('/static/<filename:path>')
# def send_static(filename):
# 	return static_file(filename, root='/path/to/static/files')


# HTTP Headers

# All HTTP headers sent by the client (Referrer, Agent, or Accept-Language) are
# accessible through the BaseRequest.headers attribute:

# from bottle import route, request
# @route('/is_ajax')
# def is_ajax():
# 	if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
# 		return 'This is an AJAX request'
# 	else:
# 		return 'This is a normal request'



# the run() call starts a built-in development server
# debug should be switched to False for public applications
run(host='localhost', port=8080, debug=True)


# reference: http://bottlepy.org/docs/dev/tutorial.html