class PlannerAgent:

    def generate_test_cases(self, requirement):

        requirement = requirement.lower()

        if "login" in requirement:
            return [
                {
                    "id": 1,
                    "title": "Valid Login",
                    "expected_result": "User should login successfully"
                },
                {
                    "id": 2,
                    "title": "Invalid Password",
                    "expected_result": "Login should fail"
                },
                {
                    "id": 3,
                    "title": "Empty Credentials",
                    "expected_result": "Login should not proceed"
                }
            ]

        if "registration" in requirement:
            return [
                {
                    "id": 1,
                    "title": "Valid Registration",
                    "expected_result": "Account should be created"
                },
                {
                    "id": 2,
                    "title": "Duplicate Email",
                    "expected_result": "Registration should fail"
                },
                {
                    "id": 3,
                    "title": "Empty Fields",
                    "expected_result": "Registration should not proceed"
                }
            ]

        return [
            {
                "id": 1,
                "title": f"Validate {requirement}",
                "expected_result": "Requirement should work"
            }
        ]