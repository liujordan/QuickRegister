# QuickRegister
## Introduction
QuickRegister is a web application that allows clubs to be easily joined by students.


## Setup

Note: This project is only tested on Python 3.5+. For Mac users, ensure you are using the correct version of Python because the OS preinstalls Python 2.7 and default `pip` and `python` commands execute in v2.7 rather than v3.x.

If you don't have Python 3 installed on your Mac, you can install [Homebrew](https://brew.sh/) and run `brew install python3` on your terminal.

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
$ pip install -r requirements.txt
```
4. Setup the superuser for `/admin` login
```
$ python manage.py createsuperuser
```

## How to run locally
1. Make sure you are in your virtualenv that you setup
```
$ source qr-env/bin/activate
```
2. Initialize database, compile scss and start server
```
$ cd quickregister
$ python manage.py migrate
$ python manage.py compilescss
$ python manage.py runserver
```
3. You can access the admin panel by going to `https://[development URL]:8000/admin/` and entering the superuser details you have created in setup.
