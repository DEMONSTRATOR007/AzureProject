from flask import Flask , render_template, request
#from textblob import TextBlob


app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print( request.form['title'] )
    
    return render_template('index.html')


@app.route("/appointment") #,methods=['GET','POST'])
def appointment():
    # if request.method == 'POST':
    #     print( request.form['title'] )
    
    return render_template('appointment.html')


@app.route("/documents")#,methods=['GET','POST'])
def documents():
    # if request.method == 'POST':
    #     print( request.form['title'] )
    
    return render_template('Appointment_details.html')

@app.route("/HealthCheckUpForm",methods=['GET','POST'])
def HealthCheckUpForm():
    return render_template('HealthCheckUpForm.html')

@app.route("/BloodTestForm") #,methods=['GET','POST'])
def BloodTestForm():
    # if request.method == 'POST':
    #     print( request.form['title'] )
    
    return render_template('BloodTestForm.html')

@app.route("/HealthCheckUpformsubmit",methods=['POST'])
def HealthCheckUpformsubmit():
    if request.method == 'POST':
       fname =  request.form.get('fname')
       lname =  request.form.get('lname')
       phone1 = request.form.get('phone1')
       phone2 = request.form.get('phone2')
       bdate = request.form.get('bdate')
       visit =  request.form.get('visit')
       date = request.form.get('date')
       visit_time = request.form.get('visit_time') 
       physician = request.form.get('physician')
       reason_for_visit = request.form.get('reason_for_visit')
      
    
    return render_template('Thank_You_appointment.html',fname =fname,lname=lname,phone1=phone1,phone2=phone2, date = date, visit_time =visit_time,physician =physician)

@app.route("/BloodTestformsubmit",methods=['POST'])
def BloodTestformsubmit():
    if request.method == 'POST':
       fname =  request.form.get('fname')
       lname =  request.form.get('lname')
       phone1 = request.form.get('phone1')
       phone2 = request.form.get('phone2')
       bdate = request.form.get('bdate')
       visit =  request.form.get('visit')
       date = request.form.get('date')
       visit_time = request.form.get('visit_time') 
       address = request.form.get('address')
       city = request.form.get('City')
       pincode = request.form.get('pincode')
    
    return render_template('Thank_You_bloodtest.html',fname =fname,lname=lname,visit_time =visit_time,date=date, address=address)

@app.route("/healthAppointmentdetails") 
def healthAppointmentdetails():
  
    return render_template('HealthCheckUp-details.html')

@app.route("/bloodAppointmentdetails")
def bloodAppointmentdetails():
    
    return render_template('bloodtest-details.html')


@app.route("/checkdetailshealth",methods=['POST'])
def checkdetailshealth():
    if request.method == 'POST':
       email_given =  request.form.get('mail')
       psw =  request.form.get('psw')
    
    return render_template('sample.html',email_given=email_given, psw = psw)

@app.route("/checkdetails_blood",methods=['POST'])
def checkdetails_blood():
    if request.method == 'POST':
       email_given =  request.form.get('mail')
       psw =  request.form.get('psw')
    return render_template('sample.html',email_given=email_given, psw = psw)



if __name__ == "__main__":
    app.run(debug=True)
