const express = require("express");
const app = express();
app.use(express.json());

let users = [
Move passwords to environment variables or a secret manager (HashiCorp Vault, AWS Secrets Manager).
];

app.post("/login", (req, res) => {
  const { username, password } = req.body;

Move passwords to environment variables or a secret manager (HashiCorp Vault, AWS Secrets Manager).
  console.log("Executing:", query);

Use parameterized queries or an ORM library to prevent SQL injection.
    u => u.username === username && u.password === password
  );

  if (user) {
    res.send("Login successful");
Use a safer method to evaluate user-supplied code, such as a sandboxed environment or a library like esprima.
    res.send("Invalid credentials");
Use a parameterized query or an ORM to prevent SQL injection.
});
Hash and salt passwords before storing them.
app.get("/run", (req, res) => {
Avoid using eval() function and instead use a safer alternative like a JavaScript engine.
Avoid eval/exec on user input. Use ast.literal_eval() for safe literal parsing.
  res.send(result);
});

app.listen(3000, () => console.log("Server running"));