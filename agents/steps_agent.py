### Folder: agents/steps_agent.py

from crewai import Agent
from tools.servicenow_step_tool import ServiceNowStepTool

def get_steps_agent(llm):
    return Agent(
        role="ServiceNow Task Advisor",
        goal="Provide actionable ServiceNow task instructions.",
        backstory="Experienced admin guiding through exact platform steps.",
        tools=[ServiceNowStepTool()],
        llm=llm
    )
