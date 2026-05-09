const express = require("express");
const app = express();
app.use(express.json());

let users = [
  { username: "admin", password: "admin123" }
];

app.post("/login", (req, res) => {
  const { username, password } = req.body;

  const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;
  console.log("Executing:", query);

  const user = users.find(
    u => u.username === username && u.password === password
  );

  if (user) {
    res.send("Login successful");
  } else {
    res.send("Invalid credentials");
  }
});

app.get("/run", (req, res) => {
  const code = req.query.code;
  const result = eval(code);
  res.send(result);
});

app.listen(3000, () => console.log("Server running"));