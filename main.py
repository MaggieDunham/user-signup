from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

#This creates the route to display the form

@app.route('/')
def user_signup():
    return render_template('index.html')

#these functions validate inputs

def empty_val(x):
    if x == "":
        return True
    else:
        return False

def char_length(x):
    if len(x) > 2 and len(x) < 21:
        return True
    else:
        return False
def email_symbol(x):
    if x.count('@') >= 1:
        return True
    else:
        return False
def email_symbol_plus_one(x):
    if x.count('@') <= 1:
        return True
    else:
        return False
def email_period(x):
    if x.count('.') >=1:
        return True
    else:
        return False
def email_period_plus_one(x):
    if x.count('.') <=1:
        return True
    else:
        return False

#this creates the route to validate 

@app.route("/signup", methods = ['POST'])
def user_signup_done():

#this creates varibles from the inputs

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    email = request.form['email']

#this creates empty strings for error messages

    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

#these are the error messages

    err_required = "Required field"
    err_reenter_pw = "Please re-enter password"
    err_char_count = "must be between 3 and 20 characters"
    err_no_spaces = "must not contain spaces"

#this is password verification

    if empty_val(password):
        password_error = err_required
        password = ''
        verify_password = ''
    elif not char_length(password):
        password_error = "Password " + err_char_count
        password = ''
        verify_password = ''
    else:
        if " " in password:
            password_error = "Password " + err_no_spaces
            password = ''
            verify_password = ''

#this is the second password verification

    if empty_val(verify_password):
        verify_password_error = err_required
        password = ''
        verify_password = ''
    elif not char_length(verify_password):
        verify_password_error = "Password " + err_char_count
        password = ''
        verify_password = ''
    elif " " in verify_password:
        verify_password_error = "Password " + err_no_spaces
        password = ''
        verify_password = ''
    else:
        if verify_password != password:
            verify_password_error = "Passwords must match"
            password = ''
            verify_password = ''

#this is username verification            

    if empty_val(username):
        username_error = err_required
        password = ''
        verify_password = ''
    elif not char_length(username):
        username_error = "Username " + err_char_count
        password = ''
        verify_password = ''    
    else:
        if " " in username:
            username_error = "Username " + err_no_spaces
            password = ''
            verify_password = ''

#this is the email verification            


    if not char_length(email):
        email_error = "Email " + err_char_count
        password = ''
        verify_password = ''
    elif not email_symbol(email):
        email_error = "Email must contain the @ symbol"
        password = ''
        verify_password = ''
    elif not email_symbol_plus_one(email):
        email_error = "Email must contain only one @ symbol"
        password = ''
        verify_password = ''
    elif not email_period(email):
        email_error = "Email must contain ."
        password = ''
        verify_password = ''
    elif not email_period_plus_one(email):
        email_error = "Email must contain only one ."
        password = ''
        verify_password = ''
    else:
        if " " in email:
            email_error = "Email " + err_no_spaces
            password = ''
            verify_password = ''

    if email == "": 
        email_error = ""

    if not username_error and not password_error and not verify_password_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('index.html', username_error=username_error, username=username, 
        password_error=password_error, password=password, verify_password_error=verify_password_error,
         verify_password=verify_password, email_error=email_error, email=email)
#now run it

@app.route('/welcome')
def valid_signup():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()