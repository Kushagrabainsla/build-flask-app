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
        {
            'type': 'checkbox',
            'name': 'views',
            'qmark': '😃',
            'message': 'Select Views',
            'choices': [
                {
                    'name': 'Auth'
                },
                {
                    'name': 'Blog'
                },
                {
                    'name': 'Error'
                }
            ]
        }
    ]

    answers = prompt(questions)

    # Creating App Directory
    parent_dir = "./"
    path = os.path.join(parent_dir, answers['appName'])
    os.mkdir(path)

    app = "./" + answers['appName']

    # Adding Essentials Files for Work.
    essentials = ['LICENSE', 'README.md', 'requirements.txt', '.gitignore']
    for item in essentials:
        filePath = os.path.join(app, item)
        with open(filePath, 'w') as fp:
            pass


    # Creating Views Folder
    views = os.path.join(app, 'Views')
    os.mkdir(views)


    # Creating Selected Views in the Views folder.
    for service in answers['views']:
        path = os.path.join(views, service)
        os.mkdir(path)
        filePath = os.path.join(path, service + '.py')
        with open(filePath, 'w') as fp:
            fp.write(filePath)
