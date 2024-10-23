const express = require('express');
const app = express();
const port = 3001;

app.get('/greeting', (req, res) => {
  res.json({ mensaje: "👋 Hi, I'm Santiago Sánchez, 🔭 I’m currently working with 🐍" });
});

app.listen(port, () => {
  console.log(`🚀 Santiago Service listening on http://localhost:${port}`);
});