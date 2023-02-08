# User Data Management

---

There is one model "User" in models.py and it contains the following fields:

- id (Datatype: Integer, Primary_Key=True)
- username (Datatype: String, Unique=True)
- birthdate (Datatype: String)
- firstname (Datatype: String)
- lastname (Datatype: String)
- email (Datatype: String)
- is_active (Datatype: Boolean, Default=False) # Activity status of the user
- password (Datatype: String) 

There is an `__init__` method in the class User which initializes all of the above mentioned fields.

Method `create_user_admin()` in main.py allows admin to create a user. An admin has the following access:

+ Can CREATE a user.

+ Can UPDATE user details.

+  Can READ user data.

+ Can DELETE a user.

To create a password, a random generator `create_password` method is used. In the future, I am going to add a `change_password` method for the user to change his password.

In the `usersignup` method, the user can sign up to the app by providing the necessary details. A feature will be added where an email will be sent to the user's email id so that he can verify himself. After verification, `is_active` field will be set to ***True***.
This method returns the `username` in ***JSON*** format.

In the `userlogin()` method, the user can login using username and password. Once user logs in, a JWT Token will be generated for the user.

In the `user_update()` method, the user will login using the JWT Token he generated. If the username in JWT Token is same as that in the url, only then will the user be confirmed and allowed to update his credentials.

The JWTToken authentication will be changed to generate a session and cookie. 

In `schemas.py`, there are two schemas present, `LoginSchema` and `UpdateSchema`.

Two new methods are to be added in `main.py`:

(1) `userview`: By this method, user can view his own profiles as well as the profiles of others.

(2) `userdelete`: By this method, user can delete his own profile from the app.