from src.agents.planner_agent import PlannerAgent

print("START")

agent = PlannerAgent()

print("OBJECT CREATED")

test_cases = agent.generate_test_cases("User Login")

print(test_cases)