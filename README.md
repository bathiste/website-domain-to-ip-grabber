# IP Logger Flask Server

A lightweight Flask-based server that captures visitor IP addresses, fetches geolocation details from [ip-api.com](http://ip-api.com), logs the information to the console in a structured format, and returns a simple HTML response to the client.

---

## Features

- Captures real client IPs (supports `X-Forwarded-For` when behind proxies like Cloudflare or Nginx).  
- Retrieves geolocation data from [ip-api.com](http://ip-api.com).  
- Logs detailed visitor information:
  - IP address  
  - Country, region, city  
  - Latitude & longitude  
  - ISP, organization, AS  
  - Timezone  
  - UTC timestamp  
- Outputs logs in a clean, styled block with auto-flush for real-time monitoring.  
- Returns a simple HTML page ("Hello") to the client.  
- Runs on any host and port (default: `0.0.0.0:5000`).  

---

## Installation

```bash
pip install flask requests
```

---

## Usage

1. Save the script as `main.py`.  
2. Run the server:

```bash
python main.py
```

3. Access the server at:

```
http://0.0.0.0:5000
```

Or on `localhost:5000`. To use a different port, set the `PORT` environment variable:

```bash
export PORT=8080  # Linux/macOS
set PORT=8080     # Windows
```

---

## Example Log Output

```
──────────────────────────────────────────────────────────────────────────────
Time       : 2025-01-01 12:00:00 UTC
Visitor IP : 8.8.8.8
Status     : Valid
Country    : United States (US)
Region     : California (CA)
Zip        : 94035
City       : Mountain View
Latitude   : 37.386
Longitude  : -122.0838
Timezone   : America/Los_Angeles
ISP        : Google LLC
Org        : Google Public DNS
AS         : AS15169 Google LLC
──────────────────────────────────────────────────────────────────────────────
```

---

## Environment Variables

| Variable | Description             | Default |
|----------|------------------------|---------|
| PORT     | Port to host the server | 5000    |

---

## Notes

- The script uses HTTP (`http://ip-api.com/json`) because the API free tier does not support HTTPS.  
- If running behind a reverse proxy, ensure `X-Forwarded-For` headers are correctly passed to capture real client IPs.  

---

## License

This project is free to use and modify.
