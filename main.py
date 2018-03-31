from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True




@app.route('/signup')
def sign_up():
    return render_template('signup.html')

@app.route('/validate-form', methods=['POST'])
def validate_form():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if username == '':
        username_error = 'You must enter a username!'
        username = ''
        if ' ' in username:
            username_error = 'username cannot contain a space'
            if password.length < 3 or password.length > 20:
                username_error = 'username length must be between 3 and 20 characters'
                username = ''

    if password == '':
        password_error ='You must enter a password'
        password = ''
        if ' ' in password:
            username_error = 'password cannot contain a space'
            username = ''
            if password.length < 3 or password.length > 20:
                username_error = 'password length must be between 3 and 20 characters'
                username = ''

    if verify_password == '':
        verify_error = 'You must verify password. Re-enter password'
        verify_password = ''
        if verify_password != password:
            verify_error = 'Passwords do not match.  Please verify password'
            verify_password = ''

    if email.count('.') > 1 or email.count('@') > 1:
        if '@' not in email or '.' not in email:
            email_error = "Invalid email address. Please enter a valid email address"

    if not username_error and not password_error and not verify_error and not email_error:
        valid = "signup was successful"
        return redirect ('/welcome?={0}'.format(valid))
    else:
        return render_template('signup.html', name=username, username_error=username_error,
                                password_error=password_error,
                                verify_error=verify_error,
                                email_error=email_error)




@app.route('/welcome')
def welcome():
    return render_template('welcome-page.html')

app.run()
