# employee_agent/agent.py
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseServerParams

# Your MCP server URL
MCP_BASE_URL = "http://gln-mule-mcp-demo.us-e1.cloudhub.io/employee-mcp-demo"

# Create the ADK Agent with MCPToolset
root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="employee_mcp_agent",
    description="Agent that connects to employee MCP server via SSE",
    instruction="You are an assistant that can fetch employee information using MCP tools. Use the available tools to search for and retrieve employee data when requested.",
    tools=[
        MCPToolset(
            connection_params=SseServerParams(
                url=MCP_BASE_URL,
                headers={}
            )
        )
    ]
)
