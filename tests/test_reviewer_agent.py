from src.agents.planner_agent import PlannerAgent
from src.agents.generator_agent import GeneratorAgent
from src.agents.reviewer_agent import ReviewerAgent

planner = PlannerAgent()
generator = GeneratorAgent()
reviewer = ReviewerAgent()

test_cases = planner.generate_test_cases("User Login")

script = generator.generate_script(test_cases)

issues = reviewer.review_script(script)

print(issues)