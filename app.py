from flask import Flask, render_template
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Define users and passwords
users = {
    "admin": "password"
}

# Verify password function
@auth.verify_password
def verify_password(username, password):
    if username in users:
        return users.get(username) == password
    return False


# Protected route
@app.route('/')
@auth.login_required
def hello_world_route():
    return render_template('hello_world.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
