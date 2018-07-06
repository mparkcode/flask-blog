import os
import sendgrid
from sendgrid.helpers.mail import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY']=os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

sg = sendgrid.SendGridAPIClient('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')





# app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'flaskblog37@gmail.com'
# app.config['MAIL_PASSWORD'] = 'Madeforflaskblog1!'
# mail = Mail(app)



from flaskblog import routes