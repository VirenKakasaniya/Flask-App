from flask import request, render_template, flash, redirect, url_for, session, current_app, Blueprint
from appFlask.webapp.forms import LoginForm
#from appFlask.__init__ import mysql, mail
#from flask_mail import Message, Mail
import requests

webapp = Blueprint('webapp', __name__)


#@app.before_first_request
#def when_someone_arrives():

@webapp.route('/')
@webapp.route('/login')
def index():
    form = LoginForm()
    form.sensor_id.data = ""
    return render_template("login.html", form=form)

@webapp.route('/aqi', methods = ['POST','GET'])
def aqi():
    form = LoginForm()
    if request.method == 'POST':
        sensor_id = request.form.get('sensor_id')


        ### GET THE TOKEN
        url_post_request = "https://secure.aqi.in/api/v1/login"
        headers_post = {'Content-Type':'application/x-www-form-urlencoded'}
        params_post = {'email':'shubhamshah7999@gmail.com', 'password':'Shubhamshah7999'}

        token_resp = requests.post(url_post_request, headers=headers_post, params= params_post)
        if token_resp.json()['status'] == 0:
            form.sensor_id.data = ""
            return render_template("login.html", error_token = True, form=form)
        else:
            bearer_auth = token_resp.json()['data']['token']

            ### check if sensor_id exists else redirect login
            url_request = "https://secure.aqi.in/api/v1/UserDeviceList/"
            headers = {'authorization': bearer_auth}
            params = {'serialNo':sensor_id}

            resp = requests.get(url_request,headers=headers, params=params)
            if resp.json()['status'] == 1:
                data = next((item for item in resp.json()['data'] if item["serialNo"] == sensor_id), None)
                if data:
                    sensor_data = data['realtime']

                    #### IF EXCEED A RANGE, SEND ALERT
                    


                    #transforming data
                    max_values = [500,500,500,100,50,100,615,3,0.05,1700,152]
                    for i in range(0,11):
                        sensor_data[i]['percentage'] = round(sensor_data[i]['sensorvalue']/max_values[i]*100)
                        if sensor_data[i]['unit'] == None:
                            sensor_data[i]['unit'] = '   '

                    return render_template("webpannel.html", sensors = sensor_data, serial_number=sensor_id)
                else:
                    form.sensor_id.data = ""
                    return render_template("login.html", error_id = True, form=form)

            else:
                return render_template("login.html", error_token = True, form=form)



    return redirect('/login')
