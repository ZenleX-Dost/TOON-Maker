# TOON-Maker Full Application

Transform simple prompts into comprehensive master prompts and token-efficient TOON format for optimal AI execution, powered by Google's Gemini LLM.

## Features

- **AI-Powered Expansion** - Uses Google Gemini (2.5/2.0/Pro) to intelligently expand prompts with context and nuance.
- **Strict TOON Format** - Generates clean, token-efficient TOON output (Task/Objective/Outcome/Narrow) without hallucinations.
- **Bilingual Support** - Full support for English and French.
- **Aggressive Premium UI** - Immersive Black & Red theme with pulsing animations, glassmorphism, and interactive elements.
- **One-Click Run** - Simple `run.bat` script to launch the full stack.
- **Real-time Processing** - Instant conversion with visual feedback.

## Tech Stack

### Backend
- **Python Flask** API
- **Google Gemini API** (`google-generativeai`) for LLM processing
- **Python Dotenv** for secure configuration
- **Strict Prompt Engineering** to enforce format constraints

### Frontend
- **React 18**
- **Aggressive CSS Design** (Black/Red theme, Glitch effects, Glowing elements)
- **Responsive Layout**

## Getting Started (User Guide)

Follow these steps to clone and run the project on your local machine.

### Prerequisites
- **Python 3.8+** installed
- **Node.js 14+** installed
- A **Google Gemini API Key** (Get one from [Google AI Studio](https://aistudio.google.com/))

### 1. Clone the Repository
```bash
git clone https://github.com/ZenleX-Dost/TOON-Maker.git
cd TOON-Maker
```

### 2. Configure Backend
1.  Navigate to the `backend` folder:
    ```bash
    cd backend
    ```
2.  Create a `.env` file (copy from `.env.example`):
    ```bash
    cp .env.example .env
    ```
3.  Open `.env` and paste your API key:
    ```env
    GEMINI_API_KEY=your_actual_api_key_here
    ```

### 3. Install Dependencies
**Backend:**
```bash
cd backend
pip install -r requirements.txt
```

**Frontend:**
```bash
cd ../frontend
npm install
```

### 4. Run the Application
You can start both the backend and frontend with a single script from the root directory:

**Windows:**
Double-click `run.bat` or run in terminal:
```bash
run.bat
```

**Manual Start:**
- Backend: `cd backend && python app.py` (Runs on `http://localhost:5000`)
- Frontend: `cd frontend && npm start` (Runs on `http://localhost:3000`)

## Usage

1.  **Enter your prompt** in the text area.
2.  **Select language** (English or French).
3.  **Click "CONVERT TO TOON FORMAT"** or press **Ctrl+Enter**.
4.  **View results**: The application will generate a strictly formatted TOON output.
5.  **Copy**: Click the copy button to save the result.

## Project Structure

```
TOON-Maker/
├── backend/
│   ├── app.py              # Flask API
│   ├── requirements.txt    # Python dependencies
│   ├── .env                # API Key (User created)
│   └── ...
├── frontend/
│   ├── src/
│   │   ├── App.js          # React Logic
│   │   ├── App.css         # Aggressive Theme Styles
│   │   └── ...
│   ├── public/
│   │   └── favicon.ico     # Custom Icon
│   └── ...
├── toon_maker.py           # Core Gemini Integration Logic
├── run.bat                 # One-click startup script
└── README.md               # Documentation
```

## Troubleshooting

-   **"TOON format generation requires AI..."**: Ensure your `GEMINI_API_KEY` is set correctly in `backend/.env`.
-   **Backend won't start**: Check if port 5000 is free.
-   **Frontend connection error**: Ensure the backend is running before using the frontend.

## License

MIT License - Developed by **Amine EL-HEND**.
