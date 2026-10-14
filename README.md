# Demonstration of AI Agent policy

We used Nemotron 3 Ultra from Openrouter.

`$env:OPENROUTER_API_KEY="YOUR-API-KEY-HERE"`

To install dependencies:

`pip install fastapi uvicorn websockets openai python-dotenv`

Secured Server

For Secured Server,

`python agent_server.py`

Then for normal user client,

python user.py

To attack, we'll run attacker.py,

python attacker.py

Vulnerable Server

For vulnerable server,

python agent_vuln.py

Then for normal user client,

python user.py

To attack, we'll run attacker.py,

python attacker.py
