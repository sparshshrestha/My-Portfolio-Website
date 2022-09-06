# Import Packages
from flask import Flask, render_template, request, json
import requests
import os
from twilio.rest import Client

# Assigning secret keys
# This code only works for my replit
# You need to create your own secret keys from the API Keys for the code to work in your replit
# Create your Account SID and Auth Token at twilio.com/console
account_sid = "ACf26bb0b9d08bfc15b7652f2e265d9076"
auth_token = "71f78b101aa35e207cddfece96b707c2"

# Create app
app = Flask('app')

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/', methods =["GET", "POST"])
def message():
	# Setting environment variables
	# See http://twil.io/secure for more info
	client = Client(account_sid, auth_token)
	# Construct message from 3 APIS
	name = request.form.get("name")
	email = request.form.get("email")
	subject = request.form.get("subject")
	message = request.form.get("message")
	msg = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
	# Send the message from twilio to my number
	# Since my twilio is a free account I can only send message to my phone number
	# To send the message to another number you need to purchace a paid membership
	message = client.messages \
                .create(
                     body = msg, # Message
                     from_ = '+12054967526', # Twilio Number
                     to = '+17059884214' # My Number
                 )
	return "Message Sent Successfully"

@app.route('/index')
def about():
	return render_template("index.html")

@app.route('/thebigmacindex')
def thebigmacindex():
	return render_template("thebigmacindex.html")

@app.route('/spacestation')
def spacestation():
	return render_template("spacestation.html")

@app.route('/sms')
def sms():
	return render_template("sms.html")

@app.route('/excel')
def excel():
	return render_template("excel.html")

@app.route('/basketball')
def basketball():
	return render_template("basketball.html")

@app.route('/robotbattle')
def robotbattle():
	return render_template("robotbattle.html")

@app.route('/oilandgas')
def oilandgas():
	return render_template("oilandgas.html")

@app.route('/eletriccar')
def eletriccar():
	return render_template("eletriccar.html")

@app.route('/revenue')
def revenue():
	return render_template("revenue.html")

@app.route('/cigarette')
def cigarette():
	return render_template("cigarette.html")

@app.route('/lowincome')
def lowincome():
	return render_template("lowincome.html")

@app.route('/righttorepair')
def righttorepair():
	return render_template("righttorepair.html")

@app.route('/python')
def python():
	return render_template("python.html")

@app.route('/r')
def r():
	return render_template("r.html")

@app.route('/sql')
def sql():
	return render_template("sql.html")

@app.route('/powerbi')
def powerbi():
	return render_template("powerbi.html")

@app.route('/spreadsheet')
def spreadsheet():
	return render_template("spreadsheet.html")

@app.route('/others')
def others():
	return render_template("others.html")

app.run(host = '0.0.0.0', port = 8080, debug = True)