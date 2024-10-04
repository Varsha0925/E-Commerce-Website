
from flask import Flask, redirect, render_template, request, session, url_for,flash
import utility as util
import model as model
import imagemodel as imagemodel
import os 
app = Flask(__name__)

app.secret_key = 'development key'


@app.route('/user', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        print('Email:',email)
        if(util.checkUser(email, password)):
            session['email']=email
            session['password']=password
            session['logged_in']=True
            return redirect(url_for('search'))
        else:
            return render_template('login.html')
    return render_template('login.html')


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        if(util.addUser(email, password)):
            return redirect(url_for('login'))
        else:
            return render_template('signup.html')
    return render_template('signup.html')



@app.route('/user/search', methods=['GET', 'POST'])
def search():
    if 'logged_in' in session and session['logged_in']:
        if request.method == 'POST':
            search = request.form['search']
            recommendations = model.get_recommendations(search)
            if recommendations is not None:
                return render_template('search.html', recommendations=recommendations)
            else:
                return render_template('search.html', recommendations=None, no_data_found=True)

        return render_template('search.html', recommendations=None)
    return redirect(url_for('login'))

@app.route('/user/ImageUpload', methods=['GET', 'POST'])
def imageUpload():
    if 'logged_in' in session and session['logged_in']:
        if request.method == 'POST':
            file = request.files['file']
            if file:
                output=imagemodel.predict_object_from_request(file)
                result=output
                output=model.get_recommendations(output)
                return render_template('image.html',recommendations=output,result=result,no_data_found=True)
            else:
                return render_template('image.html',recommendations=None, no_data_found=True,result=None)
        return render_template('image.html',recommendations=None, no_data_found=True,result=None)
    return redirect(url_for('login'))

@app.route('/user/logout')
def logout():
    session.pop('email', None)
    session.pop('password', None)
    session['logged_in'] = False
    return redirect(url_for('index'))

app.run(debug=True)