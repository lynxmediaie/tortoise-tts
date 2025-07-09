# python script to run curl request with JSON data
import requests
import json
import os

# sample curl -X POST "http://localhost:8000/tts" -H "Content-Type: application/json" -d {  "text": "Hello, this is a test of the text-to-speech system.",  "voice": "random",  "preset": "fast",  "use_deepspeed": false,  "kv_cache": true,  "half": true,  "output_path": "results",  "model_dir": "models",  "candidates": 3,  "seed": 56343,  "produce_debug_state": true,  "cvvp_amount": 0.0}
def run_curl_request():
    url = "http://localhost:8000/tts"
    headers = {"Content-Type": "application/json"}

    file_path = "./1wav.txt"

    data = {
        "voice": "zebrak",
        "preset": "high_quality",
        "kv_cache": True,
        "half": True,
        "output_path": "/app/results",
        "model_dir": "models",
        "candidates": 3,
        "seed": 56343,
        "produce_debug_state": True,
        "cvvp_amount": 0.0
    }

    with open(file_path, "rb") as f:
        files = {"file": (file_path, f)}
        response = requests.post(url, headers=headers, data=json.dumps(data), files=files)

    if response.status_code == 200:
        print("Request was successful.")
    else:
        print(f"Request failed with status code: {response.status_code}")

    print("Response:", response.text)

if __name__ == "__main__":
    run_curl_request()