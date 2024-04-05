from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail, Message
import os


app = Flask(__name__, static_url_path = '/static')

#EmailStuff 
#app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
#app.config['MAIL_PORT'] = 2525
#app.config['MAIL_USERNAME'] = 'your_email@example.com'
#app.config['MAIL_PASSWORD'] = 'your_password'
#app.config['MAIL_USE_TLS'] = True
#app.config['MAIL_USE_SSL'] = False
#mail = Mail(app)


#urlval = Databaser()

#app.config['SQLALCHEMY_DATABASE_URI'] = urlval.uri()
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#db = SQLAlchemy(app)

#class Projects(db.Model):
 #   __tablename__ = 'projects'
  #  id_projects = db.Column(db.Integer, primary_key=True)
   # project_name = db.Column(db.String(50))
    #last_updated = db.Column(db.DateTime)
    #first_updated = db.Column(db.DateTime)
    #proj_description = db.Column(db.String(250))
    #tech_used = db.Column(db.String(100))
    #github = db.Column(db.String(100))



@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html', changeTheme='')

@app.route('/services-offered')
def services():
    return render_template('services.html', changeTheme='')

@app.route('/past-projects', methods = ['GET'])
def projects():
    #projects = Projects.query.order_by(Projects.first_updated).all()
    return render_template('projects.html', posted_proj = projects, changeTheme='')

@app.route('/about-me')
def about():
    return render_template('aboutme.html')

@app.route('/contact-me', methods = ['POST','GET'])
def contact():
    return render_template('contact.html', changeTheme='')





if __name__ == "__main__":
    #with app.app_context():
     #   db.reflect()
    app.run(debug=True)

