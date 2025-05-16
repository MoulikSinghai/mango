from crewai import Task

def get_task(agent):
    return Task(
        description="Answer the ServiceNow query using a script or a guide as per agent role.",
        expected_output="A ServiceNow script or procedure.",
        agent=agent,
        async_execution=False
    )