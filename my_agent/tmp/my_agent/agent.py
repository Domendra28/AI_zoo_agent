from google.adk.agents import Agent 
from google.adk.tools import AgentTool
from google.adk.tools import google_search

from datetime import datetime
# Make sure your tool decorator is imported, e.g., from google.adk import tool



def current_time() -> str:
    """Returns the current date and time for the agent."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")




root_agent = Agent(
    name="Current_time_agent",
    model="gemini-3.1-flash-lite",
    description="you are an AI assistant that help user in answering every type of the query.",
    instruction = """
you are assistant to the user and you will answer  the questions and give answer in only 2 lines
""",
    tools=[current_time]
)

search_agent = Agent(
    name ="Search_agent",
    model="gemini-3.1-flash-lite", 
    description="you are an AI assistant that help user in answering every type of the query by " \
    "searching it in the google .",
    instruction = """
you are assistant to the user and you can use the google search for the answering the questions
 and give answer in only 2 lines
""",
tools=[google_search]
)
