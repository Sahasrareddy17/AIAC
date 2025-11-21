import sys
import json
import requests

#!/usr/bin/env python3
"""
task1.py

Simple GET request to a public API (JSONPlaceholder) and pretty-print the JSON response.

Usage:
    python task1.py           # fetch all posts
    python task1.py 1         # fetch post with id=1
"""

def fetch(url):
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.json()

def main():
        base = "https://jsonplaceholder.typicode.com/posts"
        url = base
        if len(sys.argv) >= 2:
                url = f"{base}/{sys.argv[1]}"
        try:
                data = fetch(url)
        except requests.RequestException as e:
                print(f"Request failed: {e}")
                sys.exit(1)

        pretty = json.dumps(data, indent=2, ensure_ascii=False)
        print(pretty)

if __name__ == "__main__":
        main()