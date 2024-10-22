from flask import current_app
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

# Define users and passwords
users = {
    "admin": "password"
}

@auth.verify_password
def verify_password(username, password):
    if current_app.config.get('TESTING'):
        return True  # Skip authentication in testing mode
    if username in users:
        return users.get(username) == password
    return False
