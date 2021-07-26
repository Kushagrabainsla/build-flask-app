from __future__ import print_function, unicode_literals
import os
# from PyInquirer import prompt, print_json

def StartProcess():
    # questions = [
    #     {
    #         'type': 'input',
    #         'name': 'appName',
    #         'message': 'What is your application name?',
    #     },
    # ]

    # answers = prompt(questions)
    gitignoreFileData = '''
# Byte-compiled / optimized / DLL files
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

    licenseFileData = ''' 
MIT License

Copyright (c) 2021 flaskr

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
'''

    setupPyFileData='''
from setuptools import setup

setup(
    name='flaskr',
    packages=['flaskr'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
'''
    
    parent_dir = "./"

    path = os.path.join(parent_dir, 'flaskr')
    os.mkdir(path)

    # App Directory.
    app = "./flaskr"

    essentials = ['LICENSE', 'README.md', 'requirements.txt', '.gitignore', 'setup.py']

    for item in essentials:
        filePath = os.path.join(app, item)
        with open(filePath, 'w') as fp:
            if item == 'LICENSE': fp.write(licenseFileData)
            if item == 'README.md': fp.write('readme is prited')
            if item == 'requirements.txt': fp.write('requirement is prited')
            if item == '.gitignore': fp.write(gitignoreFileData)
            if item == 'setup.py': fp.write(setupPyFileData)

    # Main server Directory
    flaskr = os.path.join(app, 'flaskr')
    os.mkdir(flaskr)


    
    flaskrItems = ['__init__.py', 'Views', 'Templates', 'Static']

    for item in flaskrItems:
        if item == '__init__.py':
            filePath = os.path.join(flaskr, item)
            with open(filePath, 'w') as fp:
                fp.write('''
    from flask import Flask
    app = Flask(__name__)

    from .Views import *
                ''')
        elif item == 'Views':
            views = os.path.join(flaskr, item)
            os.mkdir(views)
            filePath = os.path.join(views, '__init__.py')
            with open(filePath, 'w') as fp:
                fp.write('''
    from .demoApi1 import *
    from .demoApi2 import *
    ''')

            filePath = os.path.join(views, 'demoApi1.py')
            with open(filePath, 'w') as fp:
                fp.write('''
    from flaskr import app

    @app.route('/')
    def home():
        return 'Home !!'
                
    @app.route('/demoApi1')
    def demoApi1():
        return 'DEMO API 1 IS WORKING !!'
    ''')

            filePath = os.path.join(views, 'demoApi2.py')
            with open(filePath, 'w') as fp:
                fp.write('''
    from flaskr import app

    @app.route('/demoApi2')
    def demoApi2():
        return 'DEMO API 2 IS WORKING !!'
    ''')


        elif item == 'Templates':
            templates = os.path.join(flaskr, item)
            os.mkdir(templates)

            filePath = os.path.join(templates, 'base.html')
            with open(filePath, 'w') as fp:
                fp.write('''	
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" name="viewport" content="initial-scale=1, width=device-width">
            <title> APP TITLE</title>
        </head>
        <body>
            {% block body %} {% endblock %}
        </body>
    </html>
    ''')
            filePath = os.path.join(templates, 'error.html')
            with open(filePath, 'w') as fp:
                fp.write('''
    {% extends "base.html" %}
    {% block body %}

        <h2>Error Page</h2>

    {% endblock %}
    ''')

        elif item == 'Static':
            static = os.path.join(flaskr, item)
            os.mkdir(static)

    # Server Tests Directory
    tests = os.path.join(app, 'tests')
    os.mkdir(tests)

    testItems = ['TestAuth.py', 'TestBlog.py', 'TestDb.py']

    for item in testItems:
        filePath = os.path.join(tests, item)
        with open(filePath, 'w') as fp:
            fp.write(item)
