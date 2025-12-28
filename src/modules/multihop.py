"""
Multi-Hop Module (Baleen Pattern)
=================================
Iterative retrieval pipeline.
"""

import dspy
from ..signatures.search import HopQueryGenerator
from ..signatures.synthesis import FinalResearcher

class AuraMultiHop(dspy.Module):
    """
    AuraMultiHop implements the Baleen pattern for iterative retrieval.
    """
    
    def __init__(self, max_hops=2, k=3):
        super().__init__()
        self.max_hops = max_hops
        self.retrieve = dspy.Retrieve(k=k)
        self.generate_query = dspy.ChainOfThought(HopQueryGenerator)
        self.generate_answer = dspy.ChainOfThought(FinalResearcher)
    
    def forward(self, question):
        # Initialize context
        context = []
        
        # The Retrieval Loop
        for hop in range(self.max_hops):
            context_str = "\n".join(context) if context else "No context yet."
            
            # Step 1: Generate query
            query_pred = self.generate_query(context=context_str, question=question)
            
            # Step 2: Retrieve
            retrieval_res = self.retrieve(query_pred.search_query)
            
            # Step 3: Accumulate
            for p in retrieval_res.passages:
                if p not in context:
                    context.append(p)
        
        # Final Step: Synthesis
        full_context_str = "\n".join(context)
        answer_pred = self.generate_answer(context=full_context_str, question=question)
        
        return dspy.Prediction(
            context=context,
            answer=answer_pred.answer
        )
