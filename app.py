import os
from flask import Flask

app = Flask(__name__)

# Modern asynchronous route handling for concurrent traffic
@app.route("/")
def home():
    return """
    <h1 style='text-align:center;margin-top:100px;color:#fe2c55;font-family:sans-serif;'>
        TikTok Studio Pro<br>LIVE 24/7 - ONLINE
    </h1>
    <p style='text-align:center;font-family:sans-serif;color:#555;'>Your server works perfectly!</p>
    """

if __name__ == "__main__":
    # Dynamically reads the PORT assigned by cloud hosts, fallback to 10000 locally
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
