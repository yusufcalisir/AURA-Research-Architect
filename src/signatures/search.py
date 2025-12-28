"""
Search Signatures
=================
Declarative definitions for query generation.
"""

import dspy

class GenerateSearchQuery(dspy.Signature):
    """Transform a high-level research goal into an optimized search query."""
    research_goal = dspy.InputField(desc="The complex, high-level research objective")
    search_query = dspy.OutputField(desc="A keyword-optimized query for retrieval")

class HopQueryGenerator(dspy.Signature):
    """Generate a search query based on what we already know (context) and what we still need to know."""
    context = dspy.InputField(desc="The accumulated knowledge from previous retrieval hops")
    question = dspy.InputField(desc="The original complex research question")
    search_query = dspy.OutputField(desc="A targeted search query to fill information gaps")
