from __future__ import print_function, unicode_literals
import os
from PyInquirer import prompt, print_json

def StartProcess():
    questions = [
        {
            'type': 'input',
            'name': 'appName',
            'message': 'What is your application name?',
        },
    ]

    answers = prompt(questions)

    parent_dir = "./"

    path = os.path.join(parent_dir, answers['appName'])
    os.mkdir(path)

    # App Directory.
    app = "./" + answers['appName']

    essentials = ['LICENSE', 'README.md', 'requirements.txt', '.gitignore', 'setup.py']

    for item in essentials:
        filePath = os.path.join(app, item)
        with open(filePath, 'w') as fp:
            if item == 'LICENSE': fp.write('license is prited')
            if item == 'README.md': fp.write('readme is prited')
            if item == 'requirements.txt': fp.write('requirement is prited')
            if item == '.gitignore': fp.write('gitignore is prited')
            if item == 'setup.py': fp.write('setup is prited')

    # Main server Directory
    flaskr = os.path.join(app, 'flaskr')
    os.mkdir(flaskr)


    flaskrItems = ['__init__.py', 'Views', 'Templates', 'Static']

    for item in flaskrItems:
        if item == '__init__.py':
            filePath = os.path.join(flaskr, item)
            with open(filePath, 'w') as fp:
                fp.write('__init__')
        elif item == 'Views':
            views = os.path.join(flaskr, item)
            os.mkdir(views)

            # Creating Selected Views in the Views folder.
            for service in ['Auth', 'Blog', 'Db']:
                path = os.path.join(views, service)
                os.mkdir(path)
                filePath = os.path.join(path, service + '.py')
                with open(filePath, 'w') as fp:
                    fp.write(service) # Write in these files.
        elif item == 'Templates':
            templates = os.path.join(flaskr, item)
            os.mkdir(templates)

            for item in ['base.html', 'error.html']:
                filePath = os.path.join(templates, item)
                with open(filePath, 'w') as fp:
                    fp.write(item)
        elif item == 'Static':
            pass

    # Server Tests Directory
    tests = os.path.join(app, 'tests')
    os.mkdir(tests)

    testItems = ['TestAuth.py', 'TestBlog.py', 'TestDb.py']

    for item in testItems:
        filePath = os.path.join(tests, item)
        with open(filePath, 'w') as fp:
            fp.write(item)
