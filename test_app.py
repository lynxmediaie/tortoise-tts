# python script to run curl request with JSON data
import requests
import json
import os

# sample curl -X POST "http://localhost:8000/tts" -H "Content-Type: application/json" -d {  "text": "Hello, this is a test of the text-to-speech system.",  "voice": "random",  "preset": "fast",  "use_deepspeed": false,  "kv_cache": true,  "half": true,  "output_path": "results",  "model_dir": "models",  "candidates": 3,  "seed": 56343,  "produce_debug_state": true,  "cvvp_amount": 0.0}
def run_curl_request_tts():
    url = "http://localhost:8000/tts"
    headers = {"Content-Type": "application/json"}

    file_path = "/app/1wav.txt"

    data = {
        "text": "Well, I say, the pre-keramic horizon, which means in this period about those 6 thousand years, they claimed to know the ceramics, but again, as always, in our history never, one and one are two, there are always some exceptions. We know the ceramics from the 5th millennium and BC, from Peru, from the city complex El Caral, but mostly then from Usimia Valdivia. But, well, it will still talk about it, I will start to let it eat so. Just the city complex El Caral has fantastic monumental pyramids and then on the South, then there is still a nice culture that speaks Chinchorro.",
        # "file": file_path,
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

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("Request was successful.")
    else:
        print(f"Request failed with status code: {response.status_code}")

    print("Response:", response.text)

def run_curl_request_read():
    url = "http://127.0.0.1:8000/read"
    json_data = {
        "textfile": "/app/1wav.txt",
        "voice": "zebrak",
        "preset": "high_quality",
        "seed": 56343,

    }
    response = requests.post(url, json=json_data, headers={"Content-Type": "application/json"})
    print(response)

def run_curl_request_add_voice():
    url = "http://127.0.0.1:8000/add-voice/test_voice"
    response = requests.post(url, json={}, headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        print("Voice added successfully.")
    else:
        print(f"Failed to add voice. Status code: {response.status_code}")


if __name__ == "__main__":
    run_curl_request_read()
    # run_curl_request_tts()