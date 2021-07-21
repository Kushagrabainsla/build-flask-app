import sys
from build_flask_app.Components import StartProcess

def main():
    if len(sys.argv) == 1: return StartProcess()
    for arg in sys.argv:
        if arg == '-v' or arg == '--version':
            print('Version 0.0.1')
    