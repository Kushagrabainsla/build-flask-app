from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='build-flask-app',
    description='Build Flask App is an excellent open source command-line tool for beginners, which allows you to setup and run modern flask web servers efficiently by running a single command.',
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    version='0.0.7',
    license='MIT',
    author='Kushagra Bainsla',
    author_email='kushagrabainsla@gmail.com',
    url='https://github.com/Kushagrabainsla/build-flask-app',
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'pymongo',
        'Flask-PyMongo',
        'PyInquirer',
        'termcolor',
        'flask-cors',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['build-flask-app=build_flask_app.main:main'],
    },
)