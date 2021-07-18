from setuptools import setup, find_packages

setup(
    name='build-flask-app',
    packages=find_packages(),
    version='0.0.1',
    author='Kushagra Bainsla',
    author_email='kushagrabainsla@gmail.com',
    description = 'The build-flask-app is an excellent tool for beginners, which allows you to create and run Flask projects very quickly',
    url="https://github.com/Kushagrabainsla/create-flask-app",
    install_requires=['PyInquirer'],
    entry_points = {
        'console_scripts': ['build-flask-app=build_flask_app.__init__:main'],
    },
)