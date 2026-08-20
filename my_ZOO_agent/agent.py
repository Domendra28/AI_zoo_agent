from google.adk.agents import Agent 
from google.adk.tools import AgentTool
from google.adk.tools import google_search
import zoneinfo
from datetime import datetime
# Make sure your tool decorator is imported, e.g., from google.adk import tool



def current_time() -> str:
    """Returns the current date and time for the agent."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def current_time(timezone_name: str) -> str:
    """
    Returns the current date and time for a specific timezone.
    Args:
        timezone_name: The standard IANA timezone name (e.g., 'Asia/Kolkata', 'Europe/London').
    """
    try:
        # Uses Python's built-in timezone database I dont used any other library for timezone conversion.
        tz = zoneinfo.ZoneInfo(timezone_name)
        return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S %Z")
    except Exception as e:
        return f"Error finding time for {timezone_name}: {str(e)}"



  
time_agent = Agent(
    name="Current_time_agent",
    model="gemini-2.5-flash-lite",
    description="you are an AI assistant that help user in answering every type of the query.",
    instruction="""
    If the user asks for the time in a specific city, pass the city name directly to the current_time tool.
    Give the final answer in only 2 lines.
    """,
    tools=[current_time]
)
time_agent_tool =AgentTool(time_agent)





wikipedia_agent= Agent(
    name="Wikipedia_agent",
    model="gemini-2.5-flash-lite",
    description="You are an AI assistant that answers general knowledge questions by searching Wikipedia.",
    instruction="Use Wikipedia to find answers and summarize them in 2 lines.",
    tools=[google_search] # ONLY built-in tools here can be used, no custom tools are allowed in this agent
)
agent_tool = AgentTool(wikipedia_agent)

root_agent = Agent(
    name="AI_ZOO_AGENT",
    model="gemini-3.1-flash-lite",
    description="you are an AI ZOO guide assistant that help user in answering every type of the query.",
    instruction = """
you are assistant to the user and you will first greet the user like welcome to our zoo lets explore the zoo or many creative greets, then answer  the questions and give answer in only 2 lines
""",
    tools=[current_time, AgentTool(wikipedia_agent)]
)


