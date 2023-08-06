# Passwordless Client

A client library for Passwordless.dev API.

## Installation

\`\`\`bash
pip install passwordless-client
\`\`\`

## Usage

\`\`\`python
from passwordless.client import PasswordlessClient

client = PasswordlessClient(api_secret="your-api-secret")
token = client.register_token(user_id="user-id", username="username", displayname="displayname")
\`\`\`

## Documentation

Detailed documentation can be found at [link-to-your-documentation].