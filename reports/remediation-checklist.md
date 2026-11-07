# Secure Coding Remediation Checklist

- [ ] Validate all untrusted input on the server.
- [ ] Use parameterized SQL or a safe ORM; never concatenate user input into SQL.
- [ ] Encode output for its exact context (HTML, JavaScript, URL, etc.).
- [ ] Keep debug mode and detailed error traces disabled in production.
- [ ] Store secrets outside source code; do not commit `.env` files or credentials.
- [ ] Apply least privilege to database and service accounts.
- [ ] Keep dependencies updated and scan them regularly.
- [ ] Log security-relevant events without logging passwords, tokens, or sensitive data.
- [ ] Add automated tests for security controls.
- [ ] Review authorization on every protected object/action.
