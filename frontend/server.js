// Simple static server for React frontend
const express = require('express');
const path = require('path');
const app = express();

app.use(express.static(__dirname));

app.get('/*', (req, res) => {
  res.sendFile(path.resolve(__dirname, 'index.html'));
});

app.listen(3000, () => {
  console.log('Frontend running on http://localhost:3000');
});
