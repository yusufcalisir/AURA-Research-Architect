"""
AURA Configuration
==================
Centralized configuration for the AURA project.
"""

import os
import dspy

class Config:
    # API Keys
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    
    # Models
    DEFAULT_LM_MODEL = "gpt-3.5-turbo"
    OPTIMIZER_LM_MODEL = "gpt-4o-mini" # or gpt-4
    TEACHER_LM_MODEL = "gpt-3.5-turbo"
    
    # Retrieval
    COLBERT_URL = "http://20.102.90.50:2017/wiki17_abstracts"
    
    # Paths
    ARTIFACTS_DIR = "artifacts"
    COMPILED_PROGRAMS_DIR = os.path.join(ARTIFACTS_DIR, "compiled_programs")
    DISTILLED_MODELS_DIR = os.path.join(ARTIFACTS_DIR, "distilled_models")

def configure_dspy(api_key: str = None, model: str = Config.DEFAULT_LM_MODEL):
    """Configures DSPy global settings."""
    key = api_key or Config.OPENAI_API_KEY
    if not key:
        print("⚠️ Warning: No API Key provided.")
    
    lm = dspy.LM(f'openai/{model}', api_key=key)
    rm = dspy.ColBERTv2(url=Config.COLBERT_URL)
    dspy.settings.configure(lm=lm, rm=rm)
    return lm, rm
