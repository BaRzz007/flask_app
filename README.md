# A Flask App
## Install flask
`pip install flask flask-mysqldb werkzeug`

## setup database 
include a .env file with the following parameters
* MYSQL_HOST - hostname (usually 'localhost' if mysql server is hosted locally)
* MYSQL_USER - username
* MYSQL_PASSWORD - password
* MYSQL_DB - name of the database
* MYSQL_PORT - port for the database

## Setup virtual environment
`python3 -m venv venv`
### for macos/Linux
`source venv/bin/activate`
### for windows
`venv\Scripts\activate`

## install required packages

`pip install -r requirements.txt`
`pip freeze` - confirm installed packages
`flask --version` - confirm flask version

## Run the ap
`python app.py`