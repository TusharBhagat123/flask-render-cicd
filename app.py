from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(message)s"
)

@app.route("/")
def home():
    return "Flask CI/CD Project is Running Successfully!"

@app.route("/predict")
def predict():
    try:
        # Dummy prediction
        return "Prediction Successful!"
    except Exception as e:
        app.logger.error(f"Prediction Error: {e}")
        return "Prediction Failed", 500

@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.exception("Unhandled Exception")
    return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(debug=True)