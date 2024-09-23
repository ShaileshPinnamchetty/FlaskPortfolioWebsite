import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail



app = Flask(__name__)

# Often people will also separate these into a separate config.py file
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#Below is the uri for postgres db running on heroku.
#If you want to switch back to sqlite db, comment out below line and uncomment the above line
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://bkeufqnxwqkkws:d8ddf5c231c4c580ceaf871f98e8f22512c36ebd256eba50460356a82e4ff448@ec2-54-158-232-223.compute-1.amazonaws.com:5432/dacajnup3odp8m"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'shailesh.pinnamchetty@gmail.com'
# app.config['MAIL_PASSWORD'] = '4862Mogi$'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_DEBUG'] = True
# app.config['MAIL_SUPPRESS_SEND'] = False
# app.config['TESTING'] = False

app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = "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"
app.config['MAIL_DEFAULT_SENDER'] = "shailesh.pinnamchetty@gmail.com"

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

app.config["UPLOAD_FOLDER"] = os.getcwd()
mail = Mail(app)


db = SQLAlchemy(app)
Migrate(app,db)

# NOTE! These imports need to come after you've defined db, otherwise you will
# get errors in your models.py files.
## Grab the blueprints from the other views.py files for each "app"
from myproject.components.views import components_blueprint
app.register_blueprint(components_blueprint, url_prefix="/components")
