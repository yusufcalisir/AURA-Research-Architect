"""
Reflector Module (Multi-Chain Comparison)
=========================================
Generate-and-Judge strategy.
"""

import dspy
from ..signatures.synthesis import ResearchSynthesizer

class AuraReflector(dspy.Module):
    """
    Replaces standard synthesis with a "Generate & Judge" loop using MultiChainComparison.
    """
    
    def __init__(self, n=3):
        super().__init__()
        self.n = n
        self.generator = dspy.ChainOfThought(ResearchSynthesizer, n=n)
        self.comparator = dspy.MultiChainComparison(ResearchSynthesizer, M=n)
    
    def forward(self, context, research_goal):
        # Step 1: Generate candidates
        generations = self.generator(
            context=context, 
            research_goal=research_goal
        )
        
        # Step 2: Compare and Select
        final_prediction = self.comparator(
            context=context,
            research_goal=research_goal,
            completions=generations.completions
        )
        
        return final_prediction
