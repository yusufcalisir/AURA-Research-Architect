"""
Synthesis Signatures
====================
Declarative definitions for insight synthesis and research answering.
"""

import dspy

class ResearchSynthesizer(dspy.Signature):
    """Synthesize retrieved context into a structured research insight."""
    context = dspy.InputField(desc="Retrieved passages from the knowledge base")
    research_goal = dspy.InputField(desc="The original research question")
    structured_insight = dspy.OutputField(desc="A reasoned, citation-backed synthesis")

class FinalResearcher(dspy.Signature):
    """Synthesize the final answer using the fully accumulated context."""
    context = dspy.InputField(desc="The complete set of retrieved passages from all hops")
    question = dspy.InputField(desc="The original research question")
    answer = dspy.OutputField(desc="A comprehensive, multi-faceted answer to the question")
