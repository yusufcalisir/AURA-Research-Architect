"""
MIPRO Optimization Pipeline
===========================
Optimizes instructions and examples using MIPRO.
"""

import sys
import os

# Robust Path Fix: Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import dspy
try:
    from dspy.teleprompt import MIPROv2 as MIPRO
except ImportError:
    from dspy.teleprompt import MIPRO

from config import configure_dspy, Config
from src.modules.rag import AuraArchitect
from evaluation.data import create_gold_dataset
from evaluation.metrics import validate_aura_insight

def run(api_key: str):
    print(">>> MIPRO Optimizer Starting...")
    configure_dspy(api_key, Config.OPTIMIZER_LM_MODEL)
    
    trainset, devset = create_gold_dataset()
    
    teleprompter = MIPRO(
        metric=validate_aura_insight,
        num_candidates=7,
        init_temperature=1.0,
        verbose=True
    )
    
    student = AuraArchitect(k=3)
    compiled_aura = teleprompter.compile(
        student=student,
        trainset=trainset,
        max_bootstrapped_demos=3,
        max_labeled_demos=3,
        num_trials=10,
        requires_permission_to_run=False
    )
    
    save_path = os.path.join(Config.COMPILED_PROGRAMS_DIR, "aura_v2_mipro.json")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    compiled_aura.save(save_path)
    print(f"saved to {save_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key", type=str)
    args = parser.parse_args()
    run(args.api_key)
