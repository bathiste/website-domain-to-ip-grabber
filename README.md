IP Logger Flask Server
This project is a lightweight Flask-based server that captures a visitor’s IP address, fetches geolocation details using the ip-api.com service, logs the information to the console in a structured format, and returns a simple HTML response to the client.

Features
Captures real client IP (supports X-Forwarded-For when behind a proxy such as Cloudflare or Nginx).
Retrieves geolocation data from ip-api.com.

Logs:
IP address
Country, region, city
Latitude & longitude
ISP, organization, AS
Timezone
Timestamp (UTC)

Outputs logs in a clean, styled block.

Returns a simple HTML page (hello) to the user.
Auto-flushing console output for clean real-time logging.
Runs on any host/port (default 0.0.0.0:5000).

Installation
pip install flask requests

Usage:
Save the script as main.py, then run:
python main.py

The server will start on:
http://0.0.0.0:5000 or on localhost:5000


(Or a different port if you set the PORT environment variable.)

Example Log Output
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 Time      : 2025-01-01 12:00:00 UTC
 Visitor IP: 92.28.26.13
 Status    : Valid
 Country   : United Kingdom (GB)
 Region    : England (ENG)
 Zip       : MK
 City      : Milton Keynes
 Latitude  : 52.0
 Longitude : -0.7
 Timezone  : Europe/London
 Isp       : Example ISP
 Org       : Example Org
 As        : AS12345 Example-AS
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Environment Variables
Variable	Description	Default
PORT	Port to host the server	5000
Notes

The script uses HTTP (ip-api.com/json) because the API’s free tier does not support HTTPS.

If you're running behind a reverse proxy, ensure X-Forwarded-For is properly configured to pass the real client IP.

License

This project is free to use and modify.
