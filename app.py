from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    ip = request.remote_addr
    ua = request.headers.get("User-Agent", "")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("vizite.txt", "a", encoding="utf-8") as f:
        f.write(f"{time} | IP: {ip} | Browser: {ua}\n")

    return "Serverul functioneaza"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
