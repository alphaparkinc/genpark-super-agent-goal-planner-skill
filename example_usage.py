from client import SuperAgentGoalPlannerClient
client = SuperAgentGoalPlannerClient()
result = client.decompose_goal("Build a competitive analysis report on AI coding tools")
print(f"Planned {result['estimated_steps']} subtasks:")
for step in result['subtask_plan']:
    print(f"  - {step}")
