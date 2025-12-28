"""
Agent Module (ReAct Paradigm)
=============================
Autonomous agent using Reason+Act logic.
"""

import dspy

class AuraAgent(dspy.Module):
    """
    AuraAgent uses dspy.ReAct to solve problems dynamically.
    """
    
    def __init__(self):
        super().__init__()
        
        # Tool 1: Retrieval
        self.retrieve_module = dspy.Retrieve(k=1)
        
        def retrieve_knowledge(query: str) -> str:
            """Search and retrieve information."""
            result = self.retrieve_module(query)
            return result.passages[0] if result.passages else "No info found."
        
        # Tool 2: Calculator
        def calculator(expression: str) -> str:
            """Evaluate mathematical expression."""
            try:
                return str(eval(expression))
            except:
                return "Error."
        
        self.tools = [retrieve_knowledge, calculator]
        self.react = dspy.ReAct("question -> answer", tools=self.tools, max_iters=5)
    
    def forward(self, question):
        return self.react(question=question)
