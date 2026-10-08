from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(
    filename="application.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


@app.route("/")
def home():
    logging.info("Home page accessed")

    return """
    <h1>AI-Assisted DevOps Demo</h1>
    <p>Application is running successfully.</p>
    """


@app.route("/error")
def error():
    try:
        result = 10 / 0
        return str(result)

    except Exception as e:
        logging.error("Application error: %s", e)
        return "An error occurred. Check application logs.", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)