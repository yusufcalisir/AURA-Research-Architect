"""
Gold Dataset
============
Creation of training and dev sets.
"""

import dspy

def create_gold_dataset():
    """
    Create dspy.Example objects for the AURA domain.
    """
    
    examples = [
        # Machine Learning & AI
        dspy.Example(
            research_goal="What are the key limitations of Federated Learning in medical imaging?",
            reference_insight="Federated Learning in medical imaging faces challenges including statistical heterogeneity...",
        ),
        dspy.Example(
            research_goal="How does the attention mechanism work in transformer architectures?",
            reference_insight="The attention mechanism computes weighted sums of value vectors...",
        ),
        # ... (Include other examples here: GPT vs BERT, Knowledge Distillation, RLHF) ...
        dspy.Example(research_goal="What are the main differences between GPT and BERT language models?", reference_insight="GPT is autoregressive..."),
        dspy.Example(research_goal="Explain knowledge distillation.", reference_insight="Transferring knowledge from teacher to student..."),
        dspy.Example(research_goal="Pros/Cons of RLHF?", reference_insight="Aligned with preference but expensive..."),
        
        # CS & Systems
        dspy.Example(research_goal="CAP Theorem implications?", reference_insight="Consistency, Availability, Partition Tolerance trade-offs..."),
        dspy.Example(research_goal="Kubernetes service discovery?", reference_insight="ClusterIP, DNS, Environment variables..."),
        dspy.Example(research_goal="Microservices security risks?", reference_insight="Attack surface, auth complexities..."),
        
        # Natural Sciences
        dspy.Example(research_goal="CRISPR-Cas9 mechanism?", reference_insight="Bacterial immune system, sgRNA guiding Cas9..."),
        dspy.Example(research_goal="mRNA vaccine mechanism?", reference_insight="Lipid nanoparticles, translation of spike protein..."),
        
        # Physics/Math
        dspy.Example(research_goal="Quantum entanglement?", reference_insight="Correlated particles affecting each other..."),
        dspy.Example(research_goal="Riemann Hypothesis significance?", reference_insight="Distribution of primes, Millennium Problem..."),
    ]
    
    # Mark inputs explicitly
    examples = [ex.with_inputs('research_goal') for ex in examples]
    
    # Split
    split_idx = int(len(examples) * 0.7)
    trainset = examples[:split_idx]
    devset = examples[split_idx:]
    
    return trainset, devset
