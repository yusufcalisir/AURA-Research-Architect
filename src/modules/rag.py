"""
RAG Module (Classic AuraArchitect)
==================================
The standard Rewrite-Retrieve-Read pipeline.
"""

import dspy
from ..signatures.search import GenerateSearchQuery
from ..signatures.synthesis import ResearchSynthesizer

class AuraArchitect(dspy.Module):
    """
    The Aura Research Architect - A DSPy Module implementing a RAG pipeline
    with ChainOfThought reasoning for query generation and synthesis.
    """
    
    def __init__(self, k=3):
        super().__init__()
        self.retrieve = dspy.Retrieve(k=k)
        self.generate_query = dspy.ChainOfThought(GenerateSearchQuery)
        self.synthesize = dspy.ChainOfThought(ResearchSynthesizer)
    
    def forward(self, research_goal):
        """
        Execute the cognitive pipeline:
        1. Generate optimized search query (with reasoning)
        2. Retrieve relevant passages
        3. Synthesize final insight (with reasoning)
        """
        # Step 1: Query Generation
        query_result = self.generate_query(research_goal=research_goal)
        
        # Step 2: Retrieval
        retrieval_result = self.retrieve(query_result.search_query)
        
        # Step 3: Synthesis
        synthesis_result = self.synthesize(
            context=retrieval_result.passages,
            research_goal=research_goal
        )
        
        return dspy.Prediction(
            query_rationale=getattr(query_result, 'rationale', "No reasoning generated"),
            search_query=query_result.search_query,
            context=retrieval_result.passages,
            synthesis_rationale=getattr(synthesis_result, 'rationale', "No reasoning generated"),
            structured_insight=synthesis_result.structured_insight
        )
