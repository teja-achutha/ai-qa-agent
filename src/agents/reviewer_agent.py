class ReviewerAgent:

    def review_script(self, script):
        issues = []

        if "assert True" in script:
            issues.append("Replace assert True with real assertions")

        if not issues:
            issues.append("No issues found")

        return issues