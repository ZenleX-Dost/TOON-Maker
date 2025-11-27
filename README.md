# TOON-Maker Full Application

Transform simple prompts into comprehensive master prompts and token-efficient TOON format for optimal AI execution.

## Features

- 🎯 **Smart Prompt Expansion** - Automatically enriches simple prompts with context, structure, and clarity
- 📝 **TOON Format Conversion** - Converts to token-efficient TOON structure (Task/Objective/Outcome/Narrow)
- 🌍 **Bilingual Support** - Full support for English and French
- 🎨 **Premium UI** - Modern design with gradients, glassmorphism, and smooth animations
- 📋 **Copy to Clipboard** - One-click copying of results
- ⌨️ **Keyboard Shortcuts** - Press Ctrl+Enter to convert quickly
- ⚡ **Real-time Processing** - Instant conversion with loading feedback

## Tech Stack

### Backend
- Python Flask API with CORS support
- Comprehensive prompt expansion logic
- Full TOON format implementation

### Frontend
- React 18 with modern hooks
- Premium CSS design with Inter font
- Responsive glassmorphism UI
- Error handling and loading states

## Installation & Setup

### Prerequisites
- Python 3.7+
- Node.js 14+
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Flask server:
```bash
python app.py
```

Backend will start on `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install Node dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

Frontend will be available at the URL shown (typically `http://localhost:3000`)

## Usage

1. **Enter your prompt** - Type any request in the text area
2. **Select language** - Choose English or French
3. **Convert** - Click the convert button or press Ctrl+Enter
4. **View results** - See your original prompt, master prompt, and TOON format
5. **Copy** - Use the copy button to save results to clipboard

### Example

**Input:** `Write a blog post about climate change`

**Output includes:**
- Original prompt
- Expanded master prompt with context and requirements
- TOON format with structured task, objective, outcome, and narrow sections

## API Endpoints

### POST /convert
Convert a prompt to TOON format

**Request:**
```json
{
  "prompt": "Your prompt here",
  "lang": "en"
}
```

**Response:**
```json
{
  "result": "Formatted output with original, master, and TOON sections"
}
```

### GET /health
Check server status

**Response:**
```json
{
  "status": "ok"
}
```

## About TOON Format

TOON (Token-Oriented Object Notation) is a token-efficient format that achieves ~40% token savings vs JSON while maintaining high accuracy. It combines:

- **YAML-like indentation** for nested objects
- **CSV-style tabular layout** for uniform arrays
- **Explicit structural metadata** ([N] lengths, {fields} headers)

The format includes four main sections:
- **T**ask - What needs to be done
- **O**bjective - Why it matters
- **O**utcome - What the result should look like
- **N**arrow - Boundaries and constraints

## Troubleshooting

### Backend won't start
- Ensure Flask and flask-cors are installed: `pip install -r requirements.txt`
- Check if port 5000 is available
- Try running with: `python -m flask run --port=5000`

### Frontend can't connect to backend
- Verify backend is running on `http://localhost:5000`
- Check browser console for CORS errors
- Ensure flask-cors is properly installed

### Module not found errors
- Backend: Run from project root or ensure PYTHONPATH is set
- Frontend: Delete `node_modules` and run `npm install` again

## Development

The application follows a clean architecture:

```
TOON-Maker/
├── backend/
│   ├── app.py              # Flask API with CORS
│   ├── requirements.txt    # Python dependencies
│   └── __init__.py
├── frontend/
│   ├── App.js              # Main React component
│   ├── App.css             # Premium styling
│   ├── index.js            # React entry point
│   ├── index.css           # Global styles
│   ├── index.html          # HTML template
│   └── package.json        # Node dependencies
├── toon_maker.py           # Core conversion logic
├── prompt.txt              # System specification
└── README.md
```

## License

MIT License - Feel free to use and modify as needed.

## Contributing

Contributions are welcome! Please ensure:
- Code follows existing style
- All features are tested
- Documentation is updated
- Both English and French support maintained
