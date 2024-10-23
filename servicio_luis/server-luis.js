const express = require('express');
const app = express();
const port = 8000;

app.get('/servicioluis', (req, res) => {
  res.json({ message: 'Servicio de Luis' });
});

app.listen(port, () => {
  console.log(`Servicio de Luis escuchando en el puerto ${port}`);
});
