class TinyAgent:
    """A minimal, modular, and educational agent framework."""

    def __init__(self):
        self.llm = None  # ch02&3
        self.memory = None  # ch04
        self.tools = None  # ch05
        self.planner = None  # ch06

    def run(self, task: str) -> str:
        """Run the agent on a task."""

        return self._step(task)

    def _step(self, task: str) -> str:
        """Perform a single step."""

        return f'Received: {task}'

    def _execute_action(self, action: str) -> str:
        """Execute a tool action."""

        return f'Executed action: {action}'


if __name__ == '__main__':
    agent = TinyAgent()
    print(agent.run('What is 2 + 3?'))
