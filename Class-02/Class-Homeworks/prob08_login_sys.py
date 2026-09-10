from numpy.ma.core import equal

admin = ("tyler", "password123")
admin_username, admin_password = admin

username = input("Enter the username: ")
password = input("Enter the password: ")

# equal(username, admin_username) iT cAn bE uSeD
if username == admin_username and password == admin_password:
    print(f"Login Successful. Welcome {admin_username}.")
else:
    print("Login Failed.")