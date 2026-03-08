# Big4Bot — Model Context Protocol (MCP) Adapter

This directory contains the official Big4Bot MCP Server. It dynamically exposes all 46 Big4Bot consulting frameworks to any MCP-compatible AI agent (e.g., Claude Desktop, Cursor, or custom MCP clients).

Because Big4Bot itself does not contain an LLM, this server utilizes a powerful **Meta-Prompting** pattern. When an AI agent calls a Big4Bot framework, the server returns the strict methodological rules and structural JSON constraints for that framework. The agent's LLM then natively performs the consulting analysis bounded by those constraints.

## Features
- **95 Dynamic Endpoints:** The server auto-registers 46 Tools, 46 Prompts, and 3 Navigation endpoints directly from the `registry/skills-index.yaml`.
- **User-Led Prompts:** Exposes all skills as MCP Prompts (e.g., `/swot_analysis`) allowing human users to manually trigger frameworks from their UI.
- **Agent-Led Tools:** Exposes all skills as MCP Tools, forcing autonomous agents to natively gather the required `input_schema` data before executing the methodology.
- **Graph Navigation:** Includes 3 specialized tools (`suggest_logically_starting_frameworks`, `suggest_downstream_frameworks`, `get_related_framework_concepts`) allowing an agent to traverse the Big4Bot dependency graph autonomously.

## Installation

Ensure you have Python 3.10+ installed.

```bash
cd adapters/mcp
pip install -r requirements.txt
```

## Running the Server

### For Local Development (MCP Inspector)
The easiest way to test the server and explicitly view the registered tools and prompts:
```bash
npx @modelcontextprotocol/inspector python server.py
```

### For Claude Desktop Integration
To allow Claude to natively use Big4Bot's consulting skills, add the following to your `claude_desktop_config.json`:

**MacOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "big4bot": {
      "command": "python",
      "args": [
        "/absolute/path/to/Big4Bot/adapters/mcp/server.py"
      ]
    }
  }
}
```

### For Cursor Integration
1. Open Cursor Settings > Features > MCP.
2. Click **+ Add New MCP Server**.
3. Set Type to `command`.
4. Name it `Big4Bot`.
5. Set the Command to: `python /absolute/path/to/Big4Bot/adapters/mcp/server.py`

## Architecture Note
This adapter utilizes the `fastmcp` SDK to run over the standard `stdio` transport layer, ensuring instant compatibility with desktop agents.
