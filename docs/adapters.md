# Platform Adapters

Big4Bot is designed to be platform-agnostic. While the core frameworks live in `domains/`, the logic for exposing these frameworks to specific LLM providers resides in `adapters/`.

## Shared Runtime
All adapters utilize a common loader and utility layer found in `adapters/shared/`:
- **`big4bot_loader.py`:** Dynamically discovers and loads skills from the filesystem.
- **`schema_utils.py`:** Handles the translation of Big4Bot JSON Schemas into provider-specific formats (e.g., OpenAI functions, Gemini declarations).
- **`config.py`:** Manages repository pathing and environment variables like `BIG4BOT_HOME`.

## Supported Adapters

### 1. Model Context Protocol (MCP)
Located in `adapters/mcp/`, this adapter implements a FastMCP server that exposes Big4Bot as a set of Tools and Prompts.
- **Tools:** Each skill is a `tool`. The adapter uses dynamic Pydantic model creation to surface `input_schema.json` directly to the agent.
- **Prompts:** Pre-configured system prompts that bundle the methodology and schemas for quick invocation.
- **Discoverability:** Includes tools for listing frameworks, describing them, and suggesting next steps in a reasoning chain.

### 2. OpenAI
Located in `adapters/openai/`, this adapter provides a `Big4BotOpenAI` client wrapper.
- **Tool Translation:** Automatically converts Big4Bot schemas into OpenAI-compatible tool definitions.
- **Structured Outputs:** Configures tools to return analysis results that agents must synthesize against the provided methodology.

### 3. Anthropic
Located in `adapters/anthropic/`, this adapter provides a `Big4BotAnthropic` client.
- **XML Tagging:** Leverages Claude's strength in XML parsing by wrapping methodology and schemas in clearly defined tags.
- **Tool Mapping:** Dynamically generates tool definitions compatible with the Anthropic SDK.

### 4. Google Gemini
Located in `adapters/gemini/`, this adapter provides a `Big4BotGemini` client.
- **Function Declarations:** Converts Big4Bot skills into `FunctionDeclaration` objects.
- **Enforcement:** Returns methodology constraints as structured results of function calls.

## Usage Pattern
Regardless of the platform, the workflow follows a consistent pattern:
1. **Initialize Client:** The adapter scales the repository via `Big4BotLoader`.
2. **Generate Tools:** The adapter produces a list of tool/function definitions.
3. **Handle Invocations:** When an agent calls a Big4Bot tool, the adapter returns the methodology and output schema constraints, forcing the agent to perform the reasoning as prescribed by the Big4Bot methodology.
