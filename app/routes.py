from flask import render_template
from .auth import auth

def init_routes(app):

    @app.route('/')
    @auth.login_required
    def hello_world_route():
        return render_template('hello_world.html')
