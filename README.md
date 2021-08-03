Install python version 3.9

sudo apt-get install -y python-pip

sudo pip install virtualenv

Now create a virtual environment for the project and install dependencies from the requirement file

virtualenv venv -p python3

source venv/bin/activate

pip install -r requirement.txt

Commands to run this application on commandline-
export FLASK_ENV=development
flask run

To run test cases- 
export FLASK_ENV=testing
python -m unittest tests/ackermann_api_test.py
python -m unittest tests/factorial_api_test.py
python -m unittest tests/fibonacci_api_test.py


How to deploy this flask application on AWS-
(1) You need Docker and AWS CLI to deploy.
(2) Create a dockerfile and put all the dependencies like 
        Setup python 3.9 image(FROM python:3.9-alpine)
        Default port
        Install dependencies from requirement.txt ....etc
(3) Create container service and deploy application


Swagger Documentation of following apis will be available on this url(assuming you use port 5000)
http://localhost:5000/api/v1/



Assumptions-
(1) I did not implemented any kind of authentication because it was not mention in the document but 
I did create structure in the header(request_id, user_uuid). If needed, we can use this to provide authentication.

(2) All the api urls contains 'v1' because in this way it can be extended to different api versions.

(3) As a monitoring tool, I have implemented logger which helps you to see logs of a api. To extend this 
further, we can use any UI tool to view this logs.

(4) I did not use any database since all the apis contains basic calculation and there is no mention of storing
data in the requirements


Application Structure-

activities(dir) 
    - validators(dir) - Contains all validators of an api
    - ackermann_activity.py - ackermann api activity class
    - factorial_activity.py - factorial api activity class
    - fibonacci_activity.py - fibonacci api activity class

app.py - 'Entry point of your app'

apis(dir) 
    -routes.py - routing defined for apis
    -resources.py - resource classes call when you hit particular api
    -request_schema.py- request params checker of apis

common(dir) - this directory contains error and response message structure base classes

repository(dir)-
    models.py - classes to define structure of reponse data

config(dir)- contains all config files(development, testing in future to deploy on prod we can create production config)

errors.py - contains all error classes
exceptions.py - contains all the exception classes
constants.py - contains constants

tests(dir) - contains test cases for all the apis





