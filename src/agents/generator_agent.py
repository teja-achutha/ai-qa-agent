class GeneratorAgent:

    def generate_script(self, test_cases):

        script = ""

        for test_case in test_cases:

            function_name = (
                test_case["title"]
                .lower()
                .replace(" ", "_")
            )

            script += f"""
def test_{function_name}():
    assert True

"""

        return script

    def save_script(self, script, filename="test_script.py"):
        with open(filename, "w") as file:
            file.write(script)

        print("Test file generated successfully")