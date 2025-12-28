"""
Model Factory - Multi-Provider Model Configurator with Retrieval Options
=========================================================================
Supports switching between Free (Local) and Paid (Cloud) models.
Default: Ollama (FREE, runs locally)
Also provides retrieval alternatives when ColBERT servers are unavailable.
"""

import dspy

class MockRetriever:
    """
    Local Mock Retriever - Returns hardcoded knowledge passages.
    Replaces the unstable public ColBERTv2 server with reliable local data.
    """
    
    # Hardcoded knowledge base about DSPy, RAG, and AI
    KNOWLEDGE_BASE = [
        {
            "long_text": "DSPy is a framework for programming language models (LMs) in a structured, modular way. It allows developers to define 'signatures' that specify input/output fields, and 'modules' that chain together reasoning steps. DSPy supports automatic prompt optimization through techniques like BootstrapFewShot and MIPRO.",
            "text": "DSPy Framework Overview"
        },
        {
            "long_text": "Retrieval-Augmented Generation (RAG) is an AI architecture that combines information retrieval with text generation. It first retrieves relevant documents from a knowledge base, then uses those documents as context for a language model to generate accurate, grounded responses. RAG reduces hallucination and improves factual accuracy.",
            "text": "RAG Systems Explained"
        },
        {
            "long_text": "AI Agents are autonomous systems that can perceive their environment, make decisions, and take actions to achieve goals. Modern AI agents often use large language models (LLMs) as their reasoning engine, combined with tools like web search, calculators, and code execution. The ReAct pattern (Reasoning + Acting) is a popular approach for building AI agents.",
            "text": "AI Agents and ReAct Pattern"
        },
        {
            "long_text": "Machine Learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed. It uses algorithms to analyze data, identify patterns, and make predictions. Common approaches include supervised learning, unsupervised learning, and reinforcement learning.",
            "text": "Machine Learning Fundamentals"
        },
        {
            "long_text": "Chain-of-Thought (CoT) prompting is a technique that encourages language models to break down complex problems into intermediate reasoning steps. This approach significantly improves performance on tasks requiring multi-step reasoning, mathematical calculations, and logical deduction.",
            "text": "Chain-of-Thought Reasoning"
        }
    ]
    
    def __init__(self, k=3):
        self.k = k
    
    def __call__(self, query, k=None):
        """
        Return relevant passages from the local knowledge base.
        For simplicity, returns the first k passages regardless of query.
        """
        num_passages = k if k is not None else self.k
        passages = self.KNOWLEDGE_BASE[:num_passages]
        
        # Return as dspy.Example objects (DSPy-compatible format)
        return [
            dspy.Example(
                long_text=p["long_text"],
                text=p["text"]
            )
            for p in passages
        ]


class ModelFactory:
    """
    Universal Model Manager for AURA.
    Provides a unified interface to switch between different LLM providers.
    """
    
    # Available providers
    PROVIDERS = {
        "ollama": "Ollama (Free/Local)",
        "deepseek": "DeepSeek",
        "openai": "OpenAI"
    }
    
    # Default models per provider
    DEFAULT_MODELS = {
        "ollama": ["llama3", "mistral", "llama2", "codellama", "phi"],
        "deepseek": ["deepseek-chat", "deepseek-coder"],
        "openai": ["gpt-3.5-turbo", "gpt-4o-mini", "gpt-4o", "gpt-4-turbo"]
    }
    
    # Retrieval options
    RETRIEVAL_OPTIONS = {
        "none": "No Retrieval (LLM Only)",
        "colbert": "ColBERTv2 (Wikipedia)",
    }
    
    @staticmethod
    def get_model(provider: str, model_name: str = None, api_key: str = None):
        """
        Get a configured LM instance based on the provider.
        
        Args:
            provider: 'ollama', 'deepseek', or 'openai'
            model_name: Specific model name (uses default if None)
            api_key: API key (required for cloud providers, ignored for Ollama)
        
        Returns:
            Configured dspy.LM instance
        """
        provider = provider.lower()
        
        if provider == "ollama":
            # FREE - Local Ollama instance
            # No API key required, runs on localhost
            model = model_name or "llama3"
            return dspy.LM(
                f"ollama_chat/{model}",
                api_base="http://localhost:11434",
                api_key=""  # No key needed
            )
        
        elif provider == "deepseek":
            # DeepSeek - OpenAI-compatible API (Budget-friendly)
            if not api_key:
                raise ValueError("DeepSeek requires an API key")
            model = model_name or "deepseek-chat"
            return dspy.LM(
                f"openai/{model}",
                api_base="https://api.deepseek.com/v1",
                api_key=api_key
            )
        
        elif provider == "openai":
            # OpenAI - Standard cloud API
            if not api_key:
                raise ValueError("OpenAI requires an API key")
            model = model_name or "gpt-3.5-turbo"
            return dspy.LM(
                f"openai/{model}",
                api_key=api_key
            )
        
        else:
            raise ValueError(f"Unknown provider: {provider}. Use 'ollama', 'deepseek', or 'openai'.")
    
    @staticmethod
    def get_retriever(retriever_type: str, url: str = None, k: int = 3):
        """
        Get a retriever instance.
        
        Args:
            retriever_type: 'mock' for local knowledge base (RECOMMENDED), 
                           'colbert' for ColBERTv2 (may be unstable)
            url: URL for ColBERTv2 server (only used for 'colbert')
            k: Number of passages to retrieve
        
        Returns:
            Retriever instance (MockRetriever or ColBERTv2)
        """
        if retriever_type == "mock" or retriever_type == "none":
            # Default: Use local mock retriever with hardcoded knowledge
            return MockRetriever(k=k)
        elif retriever_type == "colbert":
            # External: ColBERTv2 server (may be unstable)
            return dspy.ColBERTv2(url=url)
        else:
            # Fallback to mock retriever
            return MockRetriever(k=k)
    
    @staticmethod
    def get_available_models(provider: str) -> list:
        """Get list of available models for a provider."""
        return ModelFactory.DEFAULT_MODELS.get(provider.lower(), [])
    
    @staticmethod
    def requires_api_key(provider: str) -> bool:
        """Check if provider requires an API key."""
        return provider.lower() != "ollama"
