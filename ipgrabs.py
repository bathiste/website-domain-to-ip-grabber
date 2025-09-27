# save as app.py
# requires: pip install flask requests
import os
import requests
from flask import Flask, request, Response
from datetime import datetime

app = Flask(__name__)

# --- tiny helpers matching your snippet semantics ---
def Slow(text):
    # show same output on server logs. no delay for web usage.
    print(text)

def current_time_hour():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

def Continue():
    pass

def Reset():
    pass

def Error(e):
    print("Error:", repr(e))

# --- route ---
@app.route("/", methods=["GET"])
def index():
    try:
        # get real visitor IP from X-Forwarded-For if present
        xff = request.headers.get("X-Forwarded-For", "")
        if xff:
            visitor_ip = xff.split(",")[0].strip()
        else:
            visitor_ip = request.remote_addr or "Unknown"

        # log similar to your CLI flow
        map_banner = ""  # placeholder if you used a banner earlier
        Slow(map_banner)
        Slow(f"\n{current_time_hour()} Ip -> {visitor_ip}")
        Slow(f"{current_time_hour()} Search for information..")

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

        # formatted output (server log)
        out = f"""
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
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
        Slow(out)
        Continue()
        Reset()

        # return readable HTML response to visitor
        html = f"""<pre>
Visitor IP: {visitor_ip}

{out}
</pre>"""
        return Response(html, mimetype="text/html")

    except Exception as e:
        Error(e)
        return Response(f"Error: {e}", status=500, mimetype="text/plain")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
