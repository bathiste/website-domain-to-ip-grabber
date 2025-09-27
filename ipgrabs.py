from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    # try proxy header first
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    return f"Server saw IP: {ip}\n"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
