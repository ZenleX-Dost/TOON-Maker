import requests
import time
import sys

def test_convert():
    url = "http://localhost:5000/convert"
    payload = {
        "prompt": "Write a short poem about coding",
        "lang": "en"
    }
    
    print("Waiting for server to start...")
    for i in range(10):
        try:
            requests.get("http://localhost:5000/health")
            print("Server is up!")
            break
        except:
            time.sleep(1)
            print(f"Retrying... {i+1}")
    else:
        print("Server failed to start.")
        sys.exit(1)

    print(f"Sending request to {url}...")
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Success! Response received:")
            print("-" * 50)
            print(response.json()['result'])
            print("-" * 50)
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    test_convert()
