from flask import Flask
from models import db
from routes import api
from flask_jwt_extended import JWTManager  # Import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Ensure this config class is defined properly

    # Initialize the database with the app
    db.init_app(app)

    # Initialize JWTManager with the app
    jwt = JWTManager(app)

    # Register the API blueprint
    app.register_blueprint(api, url_prefix='/api')

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Define a root route for the home page
    @app.route('/')
    def home():
        return "Welcome to the Social Media API!"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)  # Run in debug mode for development
