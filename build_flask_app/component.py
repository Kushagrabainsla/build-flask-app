import os
import subprocess
from PyInquirer import prompt
from termcolor import cprint

def startProcess():
	questions = [
		{
			'type': 'input',
			'name': 'appName',
			'message': 'What is your application name?',
		},
		{
			'type': 'confirm',
			'name': 'isGitInit',
			'message': 'Do you want to initialize a local git repository?',
		},
		{
			'type': 'confirm',
			'name': 'isSocketRequired',
			'message': 'Do you want to initialize sockets?',
		},
		{
			'type': 'list',
			'name': 'database',
			'message': 'Which database client you want to use?',
			'choices': ['MongoDB', 'SQLAlchemy', 'None'],
		}
	]

	answers = prompt(questions)
 
	# Check for spaces in Application name
	name = answers['appName'].split(' ')
	if len(name) > 1: 
		cprint("No Spaces allowed in application's name !", 'red', attrs=['bold'])
		cprint("Try again with no spaces.", 'cyan', attrs=['bold'])
		return 


	readmeFileContent = '''<img src="./images/logo.sample.png" alt="Logo of the project" align="right">

# Name of the project &middot; ![Python](https://img.shields.io/badge/Language-Python-blue?style=flat&logo=python) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/your/your-project/blob/master/LICENSE)
> Additional information or tag line

A brief description of your project, what it is used for.

## Installing / Getting started

A quick introduction of the minimal setup you need to get a hello world up &
running.

```shell
commands here
```

Here you should say what actually happens when you execute the code above.

## Developing

### Built With
List main libraries, frameworks used including versions (flask, etc ...)

### Prerequisites
What is needed to set up the dev environment. For instance, global dependencies or any other tools. include download links.


### Setting up Dev

Here's a brief intro about what a developer must do in order to start developing
the project further:

```shell
git clone https://github.com/your/your-project.git
cd your-project/
packagemanager install
```

And state what happens step-by-step. If there is any virtual environment, local server or database feeder needed, explain here.

### Building

If your project needs some additional steps for the developer to build the
project after some code changes, state them here. for example:

```shell
./configure
make
make install
```

Here again you should state what actually happens when the code above gets
executed.

### Deploying / Publishing
give instructions on how to build and release a new version
In case there's some step you have to take that publishes this project to a
server, this is the right time to state it.

```shell
packagemanager deploy your-project -s server.com -u username -p password
```

And again you'd need to tell what the previous code actually does.

## Versioning

We can maybe use [SemVer](http://semver.org/) for versioning.


## Configuration

Here you should write what are all of the configurations a user can enter when using the project.

## Tests

Describe and show how to run the tests with code examples.
Explain what these tests test and why.

```shell
Give an example
```

## Style guide

Explain your code style and show how to check it.

## Api Reference

If the api is external, link to api documentation. If not describe your api including authentication methods as well as explaining all the endpoints with their required parameters.


## Database

Explaining what database (and version) has been used. Provide download links.
Documents your database design and schemas, relations etc... 

## Licensing

State what the license is and how to find the text version of the license.
'''

	gitignoreFileContent = '''# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/
'''

	licenseFileContent = ''' MIT License

Copyright (c) 2021 {appName}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''.format(appName=answers['appName'])

	requirementsFileContent = '''Flask==1.1.2
pymongo==3.11.4
Flask-SocketIO==4.3.2
Flask-Cors==3.0.10
gunicorn==20.1.0
eventlet==0.30.2
gevent==21.1.2
dnspython==1.16.0
'''

	setupPyFileContent = '''from setuptools import setup

setup(
    name='{appName}',
    packages=['{appName}'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
'''.format(appName=answers['appName'])

	parent_dir = "./"

	path = os.path.join(parent_dir, answers['appName'])
	os.mkdir(path)

	# App Directory.
	app = "./{appName}".format(appName=answers['appName'])
	cprint("Initializing {appName}".format(appName=answers['appName']), 'cyan', attrs=['bold'])



	essentials = ['LICENSE', 'README.md', 'requirements.txt', 'gitInit', '.gitignore', 'setup.py', 'Procfile', 'bootDev.sh']

	cprint("Writing essential files ...", 'cyan', attrs=['bold'])

	for item in essentials:
		if item == 'gitInit':
			if answers['isGitInit']:
				subprocess.Popen(["git","init"], cwd = './{appName}'.format(appName=answers['appName']))
			else: continue
		else:
			filePath = os.path.join(app, item)
			with open(filePath, 'w') as fp:
				if item == 'LICENSE': fp.write(licenseFileContent)
				if item == 'README.md': fp.write(readmeFileContent)
				if item == 'requirements.txt': fp.write(requirementsFileContent)
				if item == '.gitignore': fp.write(gitignoreFileContent)
				if item == 'setup.py': fp.write(setupPyFileContent)
				if item == 'bootDev.sh': fp.write('''# Development ENV
# export FLASK_APP={appName}
# export FLASK_ENV=development
# flask run

# Production ENV
gunicorn --worker-class eventlet -w 1 {appName}:app
'''.format(appName=answers['appName']))
				if item == 'Procfile': fp.write('web: gunicorn --worker-class eventlet -w 1 {appName}:app'.format(appName=answers['appName']))

	# Main server Directory
	flaskr = os.path.join(app, answers['appName'])
	os.mkdir(flaskr)




	flaskrItems = ['__init__.py', 'views', 'templates', 'static']

	for item in flaskrItems:
		if item == '__init__.py':
			cprint("Writing {}".format(item), 'cyan', attrs=['bold'])

			filePath = os.path.join(flaskr, item)
			if answers['database'].lower() == 'mongodb':
				if answers['isSocketRequired']:
					with open(filePath, 'w') as fp:
						fp.write('''from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

# For better understanding, visit: https://flask-socketio.readthedocs.io/en/latest/
socket = SocketIO(app, cors_allowed_origins="*")
CORS(app)

# For better understanding, visit: https://pymongo.readthedocs.io/en/stable/tutorial.html
client = MongoClient('mongodb://localhost:27017/')
db = client['YOUR_DATABASE_NAME']

from .views import *
''')
				else:
					with open(filePath, 'w') as fp:
						fp.write('''from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# For better understanding, visit: https://pymongo.readthedocs.io/en/stable/tutorial.html
client = MongoClient('mongodb://localhost:27017/')
db = client['YOUR_DATABASE_NAME']

from .views import *
''')
			elif answers['database'].lower() == 'sqlalchemy':
				if answers['isSocketRequired']:
					with open(filePath, 'w') as fp:
						fp.write('''from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

# For better understanding, visit: https://flask-socketio.readthedocs.io/en/latest/
socket = SocketIO(app, cors_allowed_origins="*")
CORS(app)

# For better understanding, visit: https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from .views import *
''')				
				else:
					with open(filePath, 'w') as fp:
						fp.write('''from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# For better understanding, visit: https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from .views import *
''')
			elif answers['database'].lower() == 'none':
				if answers['isSocketRequired']:
					with open(filePath, 'w') as fp:
						fp.write('''from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

# For better understanding, visit: https://flask-socketio.readthedocs.io/en/latest/
socket = SocketIO(app, cors_allowed_origins="*")
CORS(app)

from .views import *
''')
				else:
					with open(filePath, 'w') as fp:
						fp.write('''from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from .views import *
''')

		elif item == 'views':
			cprint("Writing {}".format(item), 'cyan', attrs=['bold'])
			views = os.path.join(flaskr, item)
			os.mkdir(views)
			filePath = os.path.join(views, '__init__.py')
			with open(filePath, 'w') as fp:
				fp.write('''from .home import *
from .demoApi1 import *
from .demoApi2 import *
from .demoSockets import *
''')

			filePath = os.path.join(views, 'demoApi1.py')
			with open(filePath, 'w') as fp:
				fp.write('''from .. import app, db
from flask import jsonify

@app.route('/demoApi1Route')
def demoApi1Function():
	print(db)
	return jsonify({
		'error': False,
		'message': 'DEMO API 1 IS WORKING !!'
	})
''')

			filePath = os.path.join(views, 'demoApi2.py')
			with open(filePath, 'w') as fp:
				fp.write('''from .. import app, db
from flask import jsonify

@app.route('/demoApi2Route')
def demoApi2Function():
	print(db)
	return jsonify({
		'error': False,
		'message': 'DEMO API 2 IS WORKING !!'
	})
''')

			filePath = os.path.join(views, 'home.py')
			with open(filePath, 'w') as fp:
				fp.write('''from .. import app
from flask import render_template, jsonify

@app.route('/')
def home():
	return render_template('home.html')


@app.route('/info')
def appInfo():
	return jsonify({
		'error': False,
		'allSystemsWorkingFine': True,
		'version': '0.0.1',
		'name': 'YOUR_APP_NAME',
		'author': 'AUTHOR_NAME',
		'Description': 'YOUR_APP_DESCRIPTION',
	})


@app.route('/error')
def error():
	return render_template('error.html')
''')
			filePath = os.path.join(views, 'demoSockets.py')
			with open(filePath, 'w') as fp:
				fp.write('''from .. import app, db, socket
from flask import jsonify

@app.route('/socket/socketStatus')
def socketStatus():
	return jsonify({
		'error': False,
		'message': 'Sockets are working fine.'
	})

# SOCKETS
@socket.on('connect')
def on_connect():
	pass

''')



		elif item == 'templates':
			cprint("Writing {}".format(item), 'cyan', attrs=['bold'])
			templates = os.path.join(flaskr, item)
			os.mkdir(templates)

			filePath = os.path.join(templates, 'base.html')
			with open(filePath, 'w') as fp:
				fp.write('''<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8" name="viewport" content="initial-scale=1, width=device-width">
		<title>Build Flask App</title>
		<link rel="shortcut icon" href="https://raw.githubusercontent.com/Kushagrabainsla/build-flask-app/main/assets/favicon.ico" type="image/x-icon">
		<link rel="icon" href="https://raw.githubusercontent.com/Kushagrabainsla/build-flask-app/main/assets/favicon.ico" type="image/x-icon">
		<link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
		<link rel="icon" href="data:;base64,iVBORw0KGgo=">
	</head>
	<body class="container">
		{% block body %} {% endblock %}
	</body>
</html>
''')
			filePath = os.path.join(templates, 'home.html')
			with open(filePath, 'w') as fp:
				fp.write('''{% extends "base.html" %}
{% block body %}

	<img src="https://github.com/Kushagrabainsla/build-flask-app/blob/main/assets/buildFlaskAppLogo.png?raw=true">

{% endblock %}
''')

			filePath = os.path.join(templates, 'error.html')
			with open(filePath, 'w') as fp:
				fp.write('''{% extends "base.html" %}
{% block body %}

	<h2>Error Page</h2>

{% endblock %}
''')

		elif item == 'static':
			static = os.path.join(flaskr, item)
			os.mkdir(static)

			filePath = os.path.join(static, 'styles.css')
			with open(filePath, 'w') as fp:
				fp.write('''.container {
	width: 100%;
	height: 100vh;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
}
''')


	# Server Tests Directory
	tests = os.path.join(app, 'tests')
	os.mkdir(tests)

	testItems = ['testAuth.py', 'testDb.py']
	cprint("Writing Tests", 'cyan', attrs=['bold'])
	for item in testItems:
		filePath = os.path.join(tests, item)
		with open(filePath, 'w') as fp:
			service = item[ 4:item.index('.') ]
			fp.write('# Write you test logic for {service}'.format(service=service))
