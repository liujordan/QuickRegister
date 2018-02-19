# QuickRegister
## Introduction
QuickRegister is a web application that allows clubs to be easily joined by students.


## Setup

Note: This project requires Python 3.5+

1. Clone the repository to your directory
```
$ git clone https://github.com/liujordan/QuickRegister.git
```
2. Create a virtual environment for the project and activate it. Run `pip install virtualenv` if virtualenv does not yet exist
```
$ virtualenv qr-env --python=/usr/bin/python3
$ source qr-env/bin/activate
```
3. Install the required dependecies
```
$ cd quickregister
$ pip install requirements.txt
```

## How to run
1. Make sure you are in your virtualenv that you setup
```
$ source qr-env/bin/activate
```
2. Initialize database and start server
```
$ cd quickregister
$ python3 manage.py migrate
$ python3 manage.py runserver
```
