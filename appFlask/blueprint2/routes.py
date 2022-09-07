from flask import request, render_template, flash, redirect, url_for, session, current_app, Blueprint
#from appFlask.quiz.forms import EmailForm
#from numpy.random import randint
#from datetime import timedelta, datetime
#from appFlask.__init__ import mysql, mail
#from flask_mail import Message, Mail
#import random


blueprint2 = Blueprint('blueprint2', __name__)



@blueprint2.route('/url')
def blueprint2_home():
    return "<p> working </p>"
    #return render_template("comment-allez-vous-mourir.html")


@blueprint2.route('/url2', methods = ['GET','POST'])
def blueprint_post():

    #if request.method == 'POST':

        #return render_template("reponses-mort.html",list = [mort,mort_extend,image])
    return "<p> working </p>"
