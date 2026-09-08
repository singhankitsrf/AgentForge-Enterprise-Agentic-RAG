# Security Policy

- Never commit provider keys, tokens, credentials, private documents, or customer data.
- Keep write-capable tools behind authentication, authorization, allowlists, and explicit approval.
- Treat retrieved content as untrusted input; prompt-injection defenses are layered controls, not guarantees.
- Log tool identity, arguments, policy decision, approval decision, and result for auditable actions.
- Use least-privilege credentials and separate read and write scopes.

For a real deployment, add dependency scanning, secret scanning, SAST, network egress policy, data-retention controls, and incident response procedures.
