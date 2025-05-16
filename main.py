from crewai import Crew
from langchain.llms import Together
from agents.script_agent import get_script_agent
from agents.steps_agent import get_steps_agent
from task.servicenow_task import get_task
from dotenv import load_dotenv
import os

load_dotenv()

llm = Together(
    model="togethercomputer/llama-2-7b-chat",
    temperature=0.5,
    together_api_key=os.getenv("TOGETHER_API_KEY")
)

script_agent = get_script_agent(llm)
steps_agent = get_steps_agent(llm)

# Choose which agent to run:
task = get_task(script_agent)  # or get_task(steps_agent)

crew = Crew(
    agents=[script_agent, steps_agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()
print("\n🤖 Final Output:\n", result)
