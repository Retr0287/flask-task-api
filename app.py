from flask import Flask, jsonify
from errors.handlers import register_error_handlers
from routes.auth_routes import auth_bp
from routes.task_routes import task_bp
from exceptions.api_exeptions import(
    NotFoundError,
    ForbiddenError,
    ValidationError
)
app=Flask(__name__)
@app.errorhandler(NotFoundError)
def handle_not_found(error):
    return jsonify({"error":str(error)}),404
@app.errorhandler(ForbiddenError)
def hanle_fornidden(error):
    return jsonify({"accses":str(error)}), 403
@app.errorhandler(ValidationError)
def handle_validation(error):
    return jsonify ({"Bad":str(error)}), 400
register_error_handlers(app)
app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)
        
if __name__ == "__main__": 
    app.run(debug=True)
