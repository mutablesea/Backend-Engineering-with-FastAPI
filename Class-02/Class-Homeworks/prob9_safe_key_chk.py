student = {
    "name": "Tyler",
    "id": "22",
    "email": "tyler@gmail.com"
}

if student.get("email"):
    print(f"{student.get('name')}'s Email: {student.get('email')}.")
else:
    print("Email not found.")