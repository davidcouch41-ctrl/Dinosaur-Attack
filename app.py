from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Clifford Bone Chase</h1>
    <p>Your project is deployed on Render!</p>
    <p>Note: Tkinter games cannot run in Render's browser window.</p>
    """
