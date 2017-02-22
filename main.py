#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re

form = """<form method='post'>
            <h1>Signup</h1>
            <label>Username</label> <input type='text' name='username' value='%(username)s'> <div><label>%(username_error)s</label></div>
            <br>
            <label>Password</label> <input type='text' name='password' value='%(password)s'></input> <div><label>%(password_error)s</label></div>
            <br>
            <label>Verify Password</label> <input type='text' name='verify' value='%(verify)s'></input> <div><label>%(verify_error)s</label></div>
            <br>
            <label>Email (optional)</label> <input type='text' name='email' value='%(email)s'></input> <div><label>%(email_error)s</label></div>
            <br>
            <input type='submit'/>
        </form>
        """

user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
pass_verify_re = re.compile(r"^.{3,20}$")
email_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_user(username):
    return user_re.match(username)

def valid_pass(password):
    return pass_verify_re.match(password)

def valid_pass_match(password, verify):
    if not (password == verify):
        return False
    else:
        return True

def valid_email(email):
    if (email == ""):
        return True
    else:
        return email_re.match(email)

class MainHandler(webapp2.RequestHandler):

    def build_page(self, username_error="", password_error="", verify_error="", email_error="", username="", email="", password="", verify=""):
        values = {"username_error": username_error, "password_error": password_error, "verify_error": verify_error, "email_error": email_error, "username": username, "password": password, "verify": verify, "email": email}
        self.response.write(form % values)

    def get(self):
        self.build_page()

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        checked_username = valid_user(username)
        checked_password = valid_pass(password)
        checked_verify = valid_pass_match(password, verify)
        checked_email = valid_email(email)

        error1 = ""
        error2 = ""
        error3 = ""
        error4 = ""

        if not (checked_username):
            error1 = "Invalid user name!"

        if not (checked_password):
            error2 = "Invalid password!"

        if not (checked_verify):
            error3 = "Passwords do not match!"

        if not (checked_email):
            error4 = "Invalid email format!"

        if not (checked_username and checked_password and checked_verify and checked_email):
            self.build_page(error1, error2, error3, error4, username, email)
        else:
            self.response.write("Succeeded")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
