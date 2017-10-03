import random
from flask import Flask, render_template, request
from utils import csv


#create the dictionary that will store the csv data
dict = csv.csvToDict("data/occupations.csv")

#print dict

#Render the occupations page
app=Flask(__name__)
@app.route('/')
def root():
	return render_template('base.html');
	
@app.route('/echo',methods=["GET","POST"])
def echo():
	print request.method
	print request.args
	return render_template('echo.html',reqMethod = request.method, name = request.form["username"])


if __name__ == '__main__':
	app.debug = True
	app.run()

	
