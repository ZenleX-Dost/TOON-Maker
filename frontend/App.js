import React, { useState } from 'react';
import './App.css';

function App() {
  const [prompt, setPrompt] = useState('');
  const [lang, setLang] = useState('en');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [copied, setCopied] = useState(false);

  const handleConvert = async () => {
    if (!prompt.trim()) return;

    setLoading(true);
    setResult('');
    setError('');

    try {
      const response = await fetch('http://localhost:5000/convert', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt, lang })
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Conversion failed');
      }

      setResult(data.result);
    } catch (err) {
      setError(err.message || 'Failed to connect to the server. Make sure the backend is running.');
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setPrompt('');
    setResult('');
    setError('');
    setCopied(false);
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(result);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && e.ctrlKey) {
      handleConvert();
    }
  };

  return (
    <div className="App">
      <h1>TOON-Maker Converter</h1>

      <div className="input-section">
        <label className="input-label">Your Prompt</label>
        <textarea
          value={prompt}
          onChange={e => setPrompt(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Enter your prompt here... (Ctrl+Enter to convert)"
          rows={5}
        />
      </div>

      <div className="language-selector">
        <label>
          <input
            type="radio"
            value="en"
            checked={lang === 'en'}
            onChange={() => setLang('en')}
          />
          English
        </label>
        <label>
          <input
            type="radio"
            value="fr"
            checked={lang === 'fr'}
            onChange={() => setLang('fr')}
          />
          Français
        </label>
      </div>

      <div className="actions">
        <button
          className={`convert-btn ${loading ? 'loading' : ''}`}
          onClick={handleConvert}
          disabled={loading || !prompt.trim()}
        >
          {loading && <span className="spinner"></span>}
          {loading ? 'Converting...' : 'Convert to TOON Format'}
        </button>
        <button
          className="clear-btn"
          onClick={handleClear}
          disabled={loading}
        >
          Clear
        </button>
      </div>

      {error && (
        <div className="error-message">
          ⚠️ {error}
        </div>
      )}

      {result && (
        <div className="result-section">
          <div className="result-header">
            <div className="result-title">Result</div>
            <button
              className={`copy-btn ${copied ? 'copied' : ''}`}
              onClick={handleCopy}
            >
              {copied ? '✓ Copied!' : '📋 Copy'}
            </button>
          </div>
          <div className="result-content">{result}</div>
        </div>
      )}

      <div className="footer">
        Powered by TOON Format • Press <strong>Ctrl+Enter</strong> to convert
      </div>
    </div>
  );
}

export default App;
