from db import mysql
import re
def validate_details(name,empid,email,password,cpassword,phno):
    errors={}
    username=name.split(" ")
    if not all(re.fullmatch(r"[A-Z][a-z]*", n) for n in username):
        errors['name']= "Invalid employee name"
    if not re.fullmatch(r"^[0-9]{6}$", empid):
        errors['empid'] ="Invalid employee id"
    if not re.fullmatch(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        errors['email']= "Invalid email"
    if len(password)>=8 and len(password) <= 20:
        # errors['password']="Password length should be between 8 and 20"
        if not re.search(r"[A-Z]", password):
            errors['password_uppercase']= "Doesn't contain capital letters"
        if not re.search(r"[a-z]", password):
            errors['password_lowercase']=  "Doesn't contain small letters"
        if not re.search(r"[0-9]", password):
            errors['password_digit']= "Doesn't contain digits"
        if not re.search(r"[@#$%&]", password):
            errors['password_special']=  "Doesn't contain special characters"
    else: 
        errors['password_len'] ="Length of password should be greater than 7 and less than 21"
    if cpassword != password:
        errors['cpassword']=  "Password and conform password field doesnot match"
    if not re.fullmatch(r"[6-9][0-9]{9}", phno):
        errors['phno']=  "Invalid phone number"
    if errors:
        return False,errors
    return True,errors

def user_signup(name,empid,email,password,phno):
    empid=int(empid)
    try:
        con=mysql.connect
        cur=con.cursor()
        cur.execute('select * from user where emp_id=%s',(empid,))
        res=cur.fetchone()
        if res is not None:
            return True, "User already exists. Please login to continue"
        cur.execute("insert into user(emp_id,name,password,email,phone_no) values (%s,%s,%s,%s,%s)",(empid,name,password,email,phno))
        con.commit()
        return True, "Signup Successfull! Login to continue"
    except Exception as e:
        print('DB Error',e)
        return False, "Something went wrong. Please try again"
    finally:
        cur.close()
        con.close()
def user_login(empid,password):
    empid=int(empid)
    try:
        con=mysql.connect
        cur=con.cursor()
        cur.execute("select password from user where emp_id=%s",(empid,))
        res=cur.fetchone()
        if res is None:
            return False,"New User? Signup first"
        if res['password'].strip()==password.strip():
            return True,"Welcome to homepage"
        else:
            return False , "Wrong Password.Please try again"
    except Exception as e:
        return False,"Something went wrong.Please try again"
    finally:
        cur.close()
        con.close()
def admin_login(empid,password):
    # if empid is None:
    #     return False, "None"
    if not re.fullmatch(r"^[0-9]+$", empid):
        return False, "Employee id is not in the correct format. Please enter only digits."
    empid=int(empid)
    try:
        con=mysql.connect
        cur=con.cursor()
        cur.execute("select password from admins where emp_id=%s",(empid,))
        res=cur.fetchone()
        if res is None:
            return False,"You don't have admin privelages "
        if res['password'].strip()==password.strip():
            return True,"Welcome to homepage"
        else:
            return False , "Wrong Password.Please try again"
    except Exception as e:
        return False,"Something went wrong.Please try again"
    finally:
        cur.close()
        con.close()

