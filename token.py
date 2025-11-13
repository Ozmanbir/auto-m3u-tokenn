import requests
import os

CLOUDFLARE_API_TOKEN = os.getenv("CF_API_TOKEN")
ZONE_ID = os.getenv("CF_ZONE_ID")
RECORD_ID = os.getenv("CF_RECORD_ID")

def update_m3u():
    headers = {
        "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
        "Content-Type": "application/json",
    }

    url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{RECORD_ID}"

    new_url = f"https://example.com/auto-m3u?token={CLOUDFLARE_API_TOKEN}"

    data = {"type": "TXT", "name": "m3u-token", "content": new_url}

    response = requests.put(url, json=data, headers=headers)

    print("Güncellendi:", response.json())

update_m3u()
