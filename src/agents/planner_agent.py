class PlannerAgent:

    def generate_test_cases(self, requirement):

        return [
            {
                "id": 1,
                "title": f"Validate {requirement}",
                "expected_result": f"{requirement} should work successfully"
            }
        ]