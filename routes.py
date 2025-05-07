
from flask import Flask,render_template,request,url_for,redirect
from db import mysql
from main import validate_details,user_signup,user_login,admin_login
proj=Flask(__name__)
@proj.route('/')
def view_landing_page():
    return render_template('landingpage1.html')
@proj.route('/userlogin',methods=['GET','POST'])
def user_login_page():
    msg=request.args.get('msg','')
    if request.method=="POST":
        empid=request.form.get('empid')
        password=request.form.get('password')
        success,msg=user_login(empid,password)
        if success:
            return render_template('foodcourt.html')
    return render_template('userlogin.html',msg=msg)
@proj.route('/usersignup',methods=['GET','POST'])
def user_signup_page():
    if request.method == "POST":
        name=request.form.get('name')
        empid=request.form.get('empid')
        email=request.form.get('email')
        password=request.form.get('password')
        cpassword=request.form.get('cpassword')
        phno=request.form.get('phno')
        result=validate_details(name,empid,email,password,cpassword,phno)
        is_valid=result[0]
        errors=result[1]
        if is_valid:
            res1=user_signup(name,empid,email,cpassword,phno)
            success=res1[0]
            msg=res1[1]
            if success:
                return redirect(url_for('user_login_page',msg=msg))
        else:
            return render_template('usersignup.html',errors=errors)
    return render_template('usersignup.html', errors={})
@proj.route('/adminlogin',methods=['GET','POST'])
def admin_login_page():
    msg=""
    if request.method == "POST":
        empid=request.form.get('empid')
        password=request.form.get('password')
        success,msg=admin_login(empid,password)
        if success:
            return render_template('adminfoodcourt.html')
    return render_template('adminlogin.html',msg=msg)
@proj.route('/adminfc')
def admin_home_page():
    return render_template('adminfoodcourt.html')
@proj.route('/foodcourt')
def foodcourt_page():
    return render_template('foodcourt.html')
@proj.route('/profile')
def profile_page():
    return render_template('profile.html')
@proj.route('/oasis')
def oasis_menu_page():
    return render_template('Oasismenus.html')
@proj.route('/annapurna')
def annapurna_menu_page():
    return render_template('Annapurna.html')
@proj.route('/arena')
def arena_menu_page():
    return render_template('Arenamenus.html')
@proj.route('/floating')
def floating_menu_page():
    return render_template('floatingrestaurant.html')
@proj.route('/magna')
def magna_menu_page():
    return render_template('Magnamenus.html')
@proj.route('/fiesta')
def fiesta_menu_page():
    return render_template('Feistamenus.html')
@proj.route('/ILA')
def ILA_menu_page():
    return render_template('ILAmenus.html')
@proj.route('/adminmanage')
def admin_manage_page():
    return render_template('adminmanage.html')
