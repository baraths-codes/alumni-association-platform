from flask import Flask,render_template,redirect,url_for #required function from flask module
#application creation 
app=Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login_page'))

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/signupchoose')
def signup_choose_page():
    return render_template('signupchoose.html')

@app.route('/signupalumni')
def signup_alumni_page():
    return render_template('signupalumini.html')

@app.route('/signupstudent')
def signup_student_page():
    return render_template('signupstudent.html')

if __name__=="__main__":
    app.run(debug=True)