class LearningPathGenerator:

    def generate(
        self,
        topic: str,
        context: dict,
    ):

        steps = []

        files = context.get(
            "files",
            []
        )

        classes = context.get(
            "classes",
            []
        )

        imports = context.get(
            "imports",
            []
        )

        for file_info in files:

            file_name = file_info["file"]

            steps.append(
                f"Read {file_name}"
            )

        for class_name in classes:

            steps.append(
                f"Review class {class_name}"
            )

        for import_name in imports:

            steps.append(
                f"Understand dependency {import_name}"
            )

        if not steps:

            steps.append(
                "No repository context found"
            )

        return {
            "topic": topic,
            "steps": steps,
        }