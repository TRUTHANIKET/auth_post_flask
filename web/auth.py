from flask import Blueprint,render_template,request,flash

auth=Blueprint('auth', __name__)

@auth.route('/login',methods=['POST','GET'])
def login():

    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>this is the logout page for the html shit </p>"

@auth.route('/sign-up',methods=['POST','GET'])
def sign_up():
    if request.method=='POST':
        name=request.form.get('text')
        email=request.form.get('email')
        password=request.form.get('password')
        if len(email)<4:
            flash("email shoud be larger",category='error')
        elif len(name)<2:
            flash("name should be larger",category='error')
        elif len(password)<7:
            flash("password should be greater than 7",category='error')
        else:
            #add user to database
            flash("your acc has been addded to the data base",category="success")
    return render_template('signup.html')