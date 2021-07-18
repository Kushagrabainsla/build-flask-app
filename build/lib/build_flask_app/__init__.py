from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json

def main():
    questions = [
        {
            'type': 'input',
            'name': 'first_name',
            'message': 'What\'s your first name',
        }
    ]

    answers = prompt(questions)
    return answers