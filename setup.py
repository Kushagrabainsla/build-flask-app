from setuptools import setup, find_packages

setup(
    name='build-flask-app',
    packages=find_packages(),
    version='0.0.5',
    license='MIT',
    author='Kushagra Bainsla',
    author_email='kushagrabainsla@gmail.com',
    url='https://github.com/Kushagrabainsla/build-flask-app',
    description = 'The build-flask-app is an excellent tool for beginners, which allows you to create and run Flask projects very quickly',
    install_requires=['PyInquirer'],
    entry_points = {
        'console_scripts': ['build-flask-app=build_flask_app.main:main'],
    },
)