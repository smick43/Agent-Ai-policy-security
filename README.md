# Agent AI Policy Security

Security-focused demonstration of agent boundary enforcement, policy isolation, and unsafe tool exposure in multi-tenant AI systems.

This project illustrates how an AI agent can be constrained by policy and how a malicious actor may attempt to bypass those controls when tool access is overly permissive.

## Overview

The repository contains two server variants:

- A secure agent server that enforces user-scoped file access and policy guardrails.
- A vulnerable agent server that demonstrates a realistic bypass scenario.

The objective is to provide a practical example of:

- agent tool design
- policy enforcement in LLM-based systems
- multi-user isolation
- unsafe tool argument handling
- attack surfaces in autonomous agent environments

## Architecture

### Secure Server

The `agent_server.py` implementation models a file-management assistant for multiple users. It applies:

- a system prompt that defines access boundaries
- file tools restricted to the authenticated user's workspace
- a constrained storage model to enforce isolation

### Vulnerable Server

The `agent_vuln.py` implementation demonstrates the same functionality without strict enforcement. It allows the model to operate on user-controlled identifiers and exposes the system to path traversal and unauthorized access.

### Attack Simulation

The `attacker.py` script simulates adversarial behavior designed to bypass the agent's intended policy and access files outside the current user's scope.

## Files

- `agent_server.py` — secure multi-tenant agent server
- `agent_vuln.py` — intentionally vulnerable comparison server
- `attacker.py` — demonstration attack client
- `user.py` — standard client for legitimate interaction
- `README.md` — project documentation

## Requirements

- Python 3.10+
- OpenRouter API key
- Required packages:

```bash
pip install fastapi uvicorn websockets openai python-dotenv
```

## Environment Setup

Set the API key before launching the project:

```powershell
$env:OPENROUTER_API_KEY="YOUR-API-KEY-HERE"
```

Or in a Unix-like shell:

```bash
export OPENROUTER_API_KEY="YOUR-API-KEY-HERE"
```

## Run the Secure Server

```bash
python agent_server.py
```

Then start a standard user client:

```bash
python user.py
```

## Run the Vulnerable Server

```bash
python agent_vuln.py
```

Then start the client again:

```bash
python user.py
```

## Attack Demonstration

To simulate a policy bypass attempt:

```bash
python attacker.py
```

## Security Principles

This project highlights several core security practices:

- Never trust model-generated arguments when they influence filesystem access.
- Enforce access control outside the LLM decision layer.
- Treat tool schemas as privileged interfaces, not user-controlled instructions.
- Validate all file paths against a strict workspace boundary.
- Separate reasoning from system-level enforcement.

## Use Case

This repository is intended for learning, demonstration, and research in:

- LLM security evaluation
- agent policy enforcement
- prompt injection resistance
- secure tool design for AI systems

## Future Enhancements

Potential extensions include:

- role-based access control
- audit logging for all tool invocations
- allowlisting for safe file types
- sandboxed execution environments
- stronger monitoring and policy evaluation

## License

This project is intended for educational and security-research use.

## Note

This repository functions as a practical security reference for evaluating policy boundaries in autonomous systems and demonstrates how access control must be enforced at the system layer rather than delegated to the model.
