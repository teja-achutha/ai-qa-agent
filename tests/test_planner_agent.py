from src.agents.planner_agent import PlannerAgent

agent = PlannerAgent()

test_cases = agent.generate_test_cases("User Login")

print(test_cases)