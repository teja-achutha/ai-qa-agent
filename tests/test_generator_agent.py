from src.agents.planner_agent import PlannerAgent
from src.agents.generator_agent import GeneratorAgent

planner = PlannerAgent()
generator = GeneratorAgent()

test_cases = planner.generate_test_cases("User Login")

script = generator.generate_script(test_cases)

generator.save_script(script)

print(script)