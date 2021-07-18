from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json

def main():
    questions = [
        {
            'type': 'input',
            'name': 'appName',
            'message': 'What is your app name?',
        },
        {
            'type': 'checkbox',
            'name': 'views',
            'qmark': '😃',
            'message': 'Select Routes',
            'choices': [
                {
                'name': 'Auth'
                },
                {
                'name': 'Blog'
                },
                {
                'name': 'Profile'
                }
            ]
        }
    ]

    answers = prompt(questions)
    return answers