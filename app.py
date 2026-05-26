from flask import Flask
from errors.handlers import register_error_handlers
from routes.auth_routes import auth_bp
from routes.task_routes import task_bp 
app=Flask(__name__)
register_error_handlers(app)
app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)
        
if __name__ == "__main__": 
    app.run(debug=True)
