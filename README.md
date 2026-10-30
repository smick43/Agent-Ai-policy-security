# Agent AI Policy Security

A demonstration of AI agent security boundaries, prompt isolation, and the risks of unsafe tool exposure in multi-tenant agent systems.

This project explores how an agent may be constrained by policy and how a malicious user can attempt to bypass those constraints when tool access is overly permissive.

## Overview

The repository contains two server variants:

- A secure agent server that enforces user-scoped file access and prompt guardrails.
- A vulnerable agent server that demonstrates a realistic policy bypass scenario.

The goal is to provide a clear, practical example of:

- agent tool design
- policy enforcement in LLM-based systems
- multi-user isolation
- unsafe tool argument handling
- attack surfaces in AI agent environments

## Architecture

### Secure Server

The `agent_server.py` implementation simulates a file-management assistant for multiple users. It uses:

- a system prompt that defines user isolation rules
- tool calls that allow file reads only within the authenticated user's workspace
- a restricted storage model to demonstrate proper access boundaries

### Vulnerable Server

The `agent_vuln.py` implementation demonstrates the same concept without strict access control. It allows the model to act on user-supplied identifiers and exposes the system to path traversal and unauthorized file access.

### Attack Simulation

The `attacker.py` script simulates adversarial behavior intended to bypass the agent's intended policy and access files outside the current user's scope.

## Files

- `agent_server.py` — secure multi-tenant agent server
- `agent_vuln.py` — intentionally vulnerable server for comparison
- `attacker.py` — demonstration attack client
- `user.py` — normal client used to interact with the agent
- `README.md` — project documentation

## Prerequisites

- Python 3.10+
- An API key for OpenRouter
- Required Python packages:

```bash
pip install fastapi uvicorn websockets openai python-dotenv
```

## Environment Setup

Set your API key before running the project:

```powershell
$env:OPENROUTER_API_KEY="YOUR-API-KEY-HERE"
```

Or in a Unix-like shell:

```bash
export OPENROUTER_API_KEY="YOUR-API-KEY-HERE"
```

## Running the Secure Server

```bash
python agent_server.py
```

Then start a normal user client:

```bash
python user.py
```

## Running the Vulnerable Server

```bash
python agent_vuln.py
```

Then start the client again:

```bash
python user.py
```

## Attack Demo

To simulate an adversarial attempt to bypass agent restrictions:

```bash
python attacker.py
```

## Security Lessons

This project highlights several important principles for AI security:

- Never trust model-generated arguments when they influence filesystem access.
- Enforce access control outside the LLM decision layer.
- Treat tool schemas as privileged interfaces, not user-controlled instructions.
- Validate all file paths against a strict, expected workspace.
- Use separation of duties between model reasoning and system-level enforcement.

## Use Case

This repository is useful for learning, demonstration, and research into:

- LLM security evaluation
- agent policy enforcement
- prompt injection resistance
- secure tool design for AI systems

## Future Improvements

Potential extensions include:

- role-based access control
- audit logging for all agent tool calls
- whitelisting for allowed file types
- sandboxed execution environments
- stronger policy evaluation and monitoring

## License

This project is intended for educational and security-research purposes.

## Professional Note

This repository is a strong example of AI safety research and can be presented as a practical security-focused system demonstrating how to reason about policy boundaries in autonomous agents.
