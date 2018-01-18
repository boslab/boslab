# Biology Open Science Labs

```boslab``` is an application to automate operations of a 
[community bio lab](https://boslab.org).

This includes:
1.  User accounts and management 
2.  Project management &#42;
3.  Fully functional LIMS &#42;
4.  Lab wiki &#42;
5.  Lab operations&#42; 
6.  Integrations with Google Drive &#42;, Slack &#42;, Github, SciNote &#42;, 
Benchling &#42;, Feedly &#42; PayPal &#42;

&#42; *incomplete*

## Code characteristics

* Tested on Python 2.6, 2.7, 3.3, 3.4, 3.5 and 3.6
* Well organized directories with lots of comments
    * app
        * commands
        * models
        * static
        * templates
        * views
    * tests
* Includes test framework (`py.test` and `tox`)
* Includes database migration framework (`alembic`)
* Sends error emails to admins for unhandled exceptions


## Setting up a development environment

We assume that you are running `Python 3+`, and have `git` installed.

1. Clone the code repository into ~/Projects
```bash
$ mkdir -p ~/dev
$ cd ~/dev
$ git clone https://github.com/boslab/boslab
```
2. Create a virtual environment using Python3's `pyvenv`
```bash
$ cd ~/Projects/boslab/
$ python3 -m venv venv
$ source venv/bin/activate # activate virtual environment
```
3. Install required Python packages.
```bash
(venv)$ pip install -r requirements.txt
```

    
# Configuring SMTP

Copy the `local_settings_example.py` file to `local_settings.py`.

    cp app/local_settings_example.py app/local_settings.py

Edit the `local_settings.py` file.

Specifically set all the MAIL_... settings to match your SMTP settings

Note that Google's SMTP server requires the configuration of "less secure apps".
See https://support.google.com/accounts/answer/6010255?hl=en

Note that Yahoo's SMTP server requires the configuration of "Allow apps that use less secure sign in".
See https://help.yahoo.com/kb/SLN27791.html


## Initializing the Database

    # Create DB tables and populate the roles and users tables
    python manage.py init_db

    # Or if you have Fabric installed:
    fab init_db


## Running the app

    # Start the Flask development web server
    python manage.py runserver

    # Or if you have Fabric installed:
    fab runserver

Point your web browser to http://localhost:5000/

You can make use of the following users:
- email `user@example.com` with password `Password1`.
- email `admin@example.com` with password `Password1`.


## Running the automated tests

    # Start the Flask development web server
    py.test tests/

    # Or if you have Fabric installed:
    fab test


## Trouble shooting

If you make changes in the Models and run into DB schema issues, delete the sqlite DB file `app.sqlite`.


## Acknowledgements

With thanks to the following Flask extensions:

* [Alembic](http://alembic.zzzcomputing.com/)
* [Flask](http://flask.pocoo.org/)
* [Flask-Login](https://flask-login.readthedocs.io/)
* [Flask-Migrate](https://flask-migrate.readthedocs.io/)
* [Flask-Script](https://flask-script.readthedocs.io/)
* [Flask-User](http://flask-user.readthedocs.io/en/v0.6/)

## Authors

- Francis Lee -- francis AT boslab DOT org
- Timothy Stiles -- tim AT boslab DOT org