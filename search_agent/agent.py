from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.adk.tools import AgentTool
from datetime import datetime
import zoneinfo

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


search_agent = Agent(
    name="Search_agent",
    model="gemini-2.5-flash-lite",
    description="You are an AI assistant that answers general knowledge questions by searching Google.",
    instruction="Use Google search to find answers and summarize them in 2 lines.",
    tools=[google_search] # ONLY built-in tools here can be used, no custom tools are allowed in this agent
)
search_agent_tool = AgentTool(search_agent)





root_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[search_agent_tool,time_agent_tool]
)


