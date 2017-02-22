import re

user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
pass_verify_re = re.compile(r"^.{3,20}$")
email_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_user(username):
    return user_re.match(username)

def valid_pass_verify(password):
    return pass_verify_re.match(password)

def valid_email(email):
    return email_re.match(email)
