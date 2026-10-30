# Agent AI Policy Security

A focused security review of agent boundary enforcement, prompt isolation, and unsafe tool exposure in multi-tenant AI systems.

This project demonstrates how an AI agent may be constrained by policy and how unauthorized access can occur when tool interfaces are overly permissive. The objective is to provide a practical example of agent security design, access enforcement, and adversarial misuse in AI-driven environments.

## Overview

The repository contains two server implementations:

- A secure agent server that enforces user-scoped file access and policy guardrails.
- A vulnerable agent server that demonstrates a realistic policy bypass scenario.

The examples highlight:

- secure agent tool design
- policy enforcement in LLM-based systems
- isolation across users and tenants
- unsafe argument validation
- attack surfaces in autonomous agent architectures

## Architecture

### Secure Server

The `agent_server.py` implementation simulates a file-management assistant for multiple users. It applies:

- a system prompt that defines access boundaries
- file tools restricted to the authenticated user's workspace
- a constrained storage model that enforces isolation

### Vulnerable Server

The `agent_vuln.py` implementation mirrors the same functional pattern without strict enforcement. It permits model operations on user-controlled identifiers and demonstrates path traversal and unauthorized access risks.

### Attack Simulation

The `attacker.py` script models adversarial behavior intended to bypass the system's intended policy and access files outside the active user's scope.

## Repository Contents

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

## Environment Configuration

Set the API key before running the project:

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

Then start a standard user client:

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

## Attack Demonstration

To simulate a policy bypass attempt:

```bash
python attacker.py
```

## Security Principles

This project reinforces several core security controls:

- Do not trust model-generated arguments when they influence filesystem access.
- Enforce access control outside the LLM decision layer.
- Treat tool interfaces as privileged system boundaries, not user-controlled instructions.
- Validate file paths against a strict and expected workspace definition.
- Separate reasoning from enforcement to reduce policy bypass risk.

## Use Case

This repository is intended for research, demonstration, and security evaluation in:

- LLM security assessment
- agent policy enforcement
- prompt injection resistance
- secure tool design for AI systems

## Future Enhancements

Potential improvements include:

- role-based access control
- audit logging for all tool invocations
- allowlisting for permitted file types
- sandboxed execution environments
- enhanced policy monitoring and evaluation

## License

This project is intended for educational and security-research use.

## Security Context

This repository provides a practical reference for evaluating the security boundary between model reasoning and system enforcement. It is designed to illustrate how policy controls fail when trust is placed in unvalidated tool arguments and permissive interfaces.
