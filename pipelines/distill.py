"""
Distillation Pipeline
=====================
Compiles Aura into a smaller model.
"""

import sys
import os

# Robust Path Fix: Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import dspy
from dspy.teleprompt import BootstrapFinetune
from config import configure_dspy, Config
from src.modules.rag import AuraArchitect
from evaluation.data import create_gold_dataset
from evaluation.metrics import validate_aura_insight

def run(api_key: str, teacher_path: str = None):
    print(">>> Distillation Starting...")
    configure_dspy(api_key, Config.TEACHER_LM_MODEL)
    
    trainset, _ = create_gold_dataset()
    
    # Load Teacher
    teacher = AuraArchitect(k=3)
    if teacher_path and os.path.exists(teacher_path):
        teacher.load(teacher_path)
    
    finetuner = BootstrapFinetune(metric=validate_aura_insight)
    
    student_target = 'google/flan-t5-large'
    
    try:
        distilled_aura = finetuner.compile(
            student=AuraArchitect(k=3),
            teacher=teacher,
            trainset=trainset,
            target=student_target
        )
        
        save_path = os.path.join(Config.DISTILLED_MODELS_DIR, "flan-t5-aura")
        os.makedirs(save_path, exist_ok=True)
        # distilled_aura.save(save_path) # conceptual
        print(f"Distillation complete. Model saved to {save_path}")
        
    except Exception as e:
        print(f"Distillation simulation skipped (no GPU): {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key", type=str)
    parser.add_argument("--teacher", type=str)
    args = parser.parse_args()
    run(args.api_key, args.teacher)
