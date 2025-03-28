def login(username, password):
    # Hardcoded credentials for demonstration purposes
    valid_username = "admin"
    valid_password = "password123"

    if username == valid_username and password == valid_password:
        return "Login successful!"
    else:
        return "Invalid credentials!"
