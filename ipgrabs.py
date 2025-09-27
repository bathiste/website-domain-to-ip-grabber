# app.py
# run: pip install flask requests
import os
import requests
from flask import Flask, request, Response
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    try:
        # pick real IP
        xff = request.headers.get("X-Forwarded-For", "")
        if xff:
            visitor_ip = xff.split(",")[0].strip()
        else:
            visitor_ip = request.remote_addr or "Unknown"

        # query ip-api
        resp = requests.get(f"http://ip-api.com/json/{visitor_ip}", timeout=6)
        api = resp.json()

        status = "Valid" if api.get("status") == "success" else "Invalid"
        country = api.get("country", "None")
        country_code = api.get("countryCode", "None")
        region = api.get("regionName", "None")
        region_code = api.get("region", "None")
        zipc = api.get("zip", "None")
        city = api.get("city", "None")
        latitude = api.get("lat", "None")
        longitude = api.get("lon", "None")
        timezone = api.get("timezone", "None")
        isp = api.get("isp", "None")
        org = api.get("org", "None")
        as_host = api.get("as", "None")

        # build block
        out = f"""
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 Time      : {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")}
 Visitor IP: {visitor_ip}
 Status    : {status}
 Country   : {country} ({country_code})
 Region    : {region} ({region_code})
 Zip       : {zipc}
 City      : {city}
 Latitude  : {latitude}
 Longitude : {longitude}
 Timezone  : {timezone}
 Isp       : {isp}
 Org       : {org}
 As        : {as_host}
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
"""

        # log to server console
        print(out)

        # return to visitor
        return Response(f"<pre>hello</pre>", mimetype="text/html")

    except Exception as e:
        print("Error:", e)
        return Response(f"Error: {e}", status=500, mimetype="text/plain")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
