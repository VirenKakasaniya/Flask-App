from flask import Flask
#from flask_mail import Message, Mail
#from flask_mysqldb import MySQL
from appFlask.config import Config


#session = Session(app)
#mysql = MySQL()
#mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from appFlask.webapp.routes import webapp
    #from appFlask.blueprint2.routes import blueprint2
    app.register_blueprint(webapp)
    #app.register_blueprint(blueprint2)

    #mail.init_app(app)
    #mysql.init_app(app)

    return app

#with app.app_context():
#    cur = mysql.connection.cursor()
#    cur.execute("""
#DROP TABLE visitors;
#CREATE TABLE visitors(
#    id INT NOT NULL PRIMARY KEY,
#    ip_address VARCHAR(20),
#    requested_url VARCHAR(50),
#    referer_page VARCHAR(50),
#    page_name VARCHAR(50),
#    query_string VARCHAR(50),
#    user_agent VARCHAR(50),
#    access_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
#    age VARCHAR(20),
#    zone_urbaine VARCHAR(30),
#    sport VARCHAR(30),
#    risque VARCHAR(30),
#    localisation_geo VARCHAR(30),
#    maladie VARCHAR(30),
#    movie VARCHAR(30),
#    profil_pers INT,
#    profil_nom VARCHAR(60),
#    nb_essais INT,
#    affect_perso VARCHAR(30),
#    affect_nextgen VARCHAR(30),
#    pb_caused_by_humans VARCHAR(30),
#    climat_num INT,
#    climat_nom VARCHAR(30),
#    ask_more VARCHAR(30),
#    email VARCHAR(30)
#    );""")
#    cur.close()
