from google.adk.agents.llm_agent import Agent

def get_current_time(city: str) -> str:
    return f"The current time in {city} is 3pm"

root_agent = Agent(
    model='gemini-flash-latest',
    name='root_agent',
    description='tell the current time in a city.',
    instruction='Your are a helpful assistant. Answer user questions for the time in the city asked. use the get_current_time tool for this purpose',
    tools=[get_current_time],
)
