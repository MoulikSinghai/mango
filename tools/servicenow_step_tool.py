### Folder: tools/servicenow_step_tool.py

from crewai_tools import BaseTool

class ServiceNowStepTool(BaseTool):
    name = "ServiceNow Step Guide"
    description = "Gives step-by-step guide to perform a ServiceNow task."

    def _run(self, query: str) -> str:
        return f"Steps to complete '{query}' in ServiceNow:\n1. Log in to ServiceNow.\n2. Navigate to the module.\n3. Follow UI to complete task.\n4. Save and validate results."