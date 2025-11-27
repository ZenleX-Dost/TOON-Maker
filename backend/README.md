# TOON-Maker Backend API

A Flask API for converting normal prompts to master prompts and TOON format.

## Endpoints

- `POST /convert`  
  Request JSON: `{ "prompt": "...", "lang": "en|fr" }`  
  Response JSON: `{ "result": "..." }`

- `GET /health`  
  Returns `{ "status": "ok" }`

## Setup

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the server:
   ```sh
   python app.py
   ```

## Usage

Send a POST request to `/convert` with a prompt and language.
