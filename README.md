Install python version 3.9

sudo apt-get install -y python-pip

sudo pip install virtualenv

Now create a virtual environment for the project and install dependencies from the requirement file

virtualenv venv -p python3

source venv/bin/activate

pip install -r requirement.txt


EXPORT FLASK_ENV=development

