import sys
from build_flask_app.component import startProcess

def main():
    if len(sys.argv) == 1: return startProcess()
        
    for arg in sys.argv:
        if arg == '-v' or arg == '--version':
            print('Version 0.0.5')

    