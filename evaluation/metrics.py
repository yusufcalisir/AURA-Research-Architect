"""
Metrics & Judges
================
AI Judges and metric functions for evaluation.
"""

import dspy

class AssessResearchQuality(dspy.Signature):
    """
    AI Judge Signature: Assess the quality of generated research insights.
    """
    context = dspy.InputField(desc="The retrieved passages from the knowledge base")
    research_goal = dspy.InputField(desc="The original research question to be answered")
    generated_insight = dspy.InputField(desc="Aura's synthesized research output")
    
    assessment_score = dspy.OutputField(desc="Quality score from 1-5")
    reasoning = dspy.OutputField(desc="Detailed explanation of the score")


class ResearchQualityJudge(dspy.Module):
    def __init__(self):
        super().__init__()
        self.assess = dspy.ChainOfThought(AssessResearchQuality)
    
    def forward(self, context, research_goal, generated_insight):
        return self.assess(
            context=context,
            research_goal=research_goal,
            generated_insight=generated_insight
        )

def validate_aura_insight(example, pred, trace=None) -> bool:
    """Metric function returning boolean (True if score >= 4)."""
    return _validate(example, pred, trace, return_bool=True)

def validate_aura_insight_with_score(example, pred, trace=None) -> float:
    """Metric function returning float score."""
    return _validate(example, pred, trace, return_bool=False)

def _validate(example, pred, trace, return_bool):
    judge = ResearchQualityJudge()
    
    # Handle context types (list vs string)
    if hasattr(pred, 'context'):
        ctx = pred.context
    else:
        # Fallback if prediction lacks context context
        ctx = "No context provided."
        
    if isinstance(ctx, list):
        context_str = "\n".join([str(p) for p in ctx])
    else:
        context_str = str(ctx)
        
    # Handle insight field name (standardizing on structured_insight, 
    # but checking answer/structured_report for compatibility)
    if hasattr(pred, 'structured_insight'):
        insight = pred.structured_insight
    elif hasattr(pred, 'answer'):
        insight = pred.answer
    elif hasattr(pred, 'structured_report'):
        insight = pred.structured_report
    else:
        insight = str(pred)

    try:
        assessment = judge(
            context=context_str,
            research_goal=example.research_goal,
            generated_insight=insight
        )
        
        score_str = str(assessment.assessment_score).strip()
        import re
        numbers = re.findall(r'[\d.]+', score_str)
        score = float(numbers[0]) if numbers else 3.0
        score = max(1.0, min(5.0, score))
        
        if trace is not None:
            print(f"Goal: {example.research_goal[:30]}... | Score: {score}")

        if return_bool:
            return score >= 4.0
        return score
        
    except Exception as e:
        print(f"Metric Error: {e}")
        return False if return_bool else 0.0
