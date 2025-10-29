from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    try:
        # Get public IP info
        ip_data = requests.get("https://ipinfo.io/json").json()
        ip = ip_data.get("ip", "Unknown IP")
        city = ip_data.get("city", "")
        region = ip_data.get("region", "")
        country = ip_data.get("country", "")
        location = f"{city}, {region}, {country}".strip(", ")
    except Exception:
        ip, location = "Unknown", "Unknown Location"

    html_content = f"""
    <html>
        <head>
            <title>Server Info</title>
            <style>
                body {{
                    background-color: black;
                    color: white;
                    font-family: monospace;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    text-align: center;
                }}
                h1 {{
                    font-size: 2.5rem;
                    line-height: 1.5;
                }}
            </style>
        </head>
        <body>
            <h1>Hello.<br>I am being served from<br>{location}<br>at<br>{ip}</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
