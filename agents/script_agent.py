### Folder: agents/script_agent.py

from crewai import Agent
from tools.servicenow_script_tool import ServiceNowScriptTool
from memory.memory_manager import get_memory

def get_script_agent(llm):
    return Agent(
        role="ServiceNow Script Developer",
        goal="Provide optimized and functional ServiceNow scripts.",
        backstory="A highly skilled developer who knows both frontend and backend of ServiceNow.",
        tools=[ServiceNowScriptTool()],
        memory=get_memory(),
        llm=llm
    )