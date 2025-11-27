from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from toon_maker import ToonMaker

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/convert', methods=['POST'])
def convert():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        prompt = data.get('prompt', '').strip()
        if not prompt:
            return jsonify({'error': 'Prompt cannot be empty'}), 400
        
        lang = data.get('lang', 'en')
        if lang not in ['en', 'fr']:
            return jsonify({'error': 'Language must be "en" or "fr"'}), 400
        
        tm = ToonMaker(language=lang)
        result = tm.process(prompt)
        return jsonify({'result': result})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
