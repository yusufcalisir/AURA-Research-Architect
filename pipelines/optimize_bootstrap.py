"""
Bootstrap Optimization Pipeline
===============================
Optimizes AuraArchitect using BootstrapFewShotWithRandomSearch.
"""

import sys
import os

# Robust Path Fix: Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import dspy
from dspy.teleprompt import BootstrapFewShotWithRandomSearch
from config import configure_dspy, Config
from src.modules.rag import AuraArchitect
from evaluation.data import create_gold_dataset
from evaluation.metrics import validate_aura_insight

def run(api_key: str):
    print(">>> MIPRO/Bootstrap Optimizer Starting...")
    configure_dspy(api_key, Config.OPTIMIZER_LM_MODEL)
    
    trainset, devset = create_gold_dataset()
    
    teleprompter = BootstrapFewShotWithRandomSearch(
        metric=validate_aura_insight,
        max_bootstrapped_demos=4,
        max_labeled_demos=4,
        num_candidate_programs=5
    )
    
    student = AuraArchitect(k=3)
    compiled_aura = teleprompter.compile(student, trainset=trainset, valset=devset)
    
    save_path = os.path.join(Config.COMPILED_PROGRAMS_DIR, "aura_v1_bootstrap.json")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    compiled_aura.save(save_path)
    print(f"saved to {save_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key", type=str)
    args = parser.parse_args()
    run(args.api_key)
