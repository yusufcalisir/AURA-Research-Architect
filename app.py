"""
Streamlit Web Interface - AURA Research Architect
==================================================
Modern glassmorphism UI with Hybrid Engine (Multi-Provider) support.
"""

import sys
import os

# Robust Path Fix: Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
import dspy
from config import Config
from src.utils.model_factory import ModelFactory
from src.modules.rag import AuraArchitect
from src.modules.multihop import AuraMultiHop
from src.modules.agent import AuraAgent
from src.modules.reflector import AuraReflector

# =============================================================================
# Page Configuration
# =============================================================================
st.set_page_config(
    page_title="AURA Research Architect",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# Custom CSS - Performance Optimized, Theme Aware
# =============================================================================
st.markdown("""
<style>
    /* Modern Font */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    /* ===== DARK MODE (Default) ===== */
    :root {
        --text-main: #f1f5f9;
        --text-sub: #94a3b8;
        --card-bg: rgba(30, 41, 59, 0.6);
        --card-border: rgba(255, 255, 255, 0.1);
    }
    
    /* ===== LIGHT MODE ===== */
    @media (prefers-color-scheme: light) {
        :root {
            --text-main: #1e293b;
            --text-sub: #475569;
            --card-bg: #f8fafc;
            --card-border: rgba(0, 0, 0, 0.08);
        }
    }

    /* Responsive scaling and fonts */
    * { 
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        box-sizing: border-box;
    }
    
    .main .block-container { 
        padding-top: 2rem; 
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 1100px; 
    }
    
    /* Hero - Gradient always visible */
    .hero-title {
        font-size: clamp(1.75rem, 8vw, 2.5rem);
        font-weight: 700;
        background: linear-gradient(135deg, #6366f1, #a855f7, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        text-align: center;
        font-size: clamp(0.9rem, 4vw, 1rem);
        margin-bottom: 2rem;
        color: var(--text-sub);
        padding: 0 1rem;
    }
    @media (prefers-color-scheme: light) {
        .hero-subtitle { color: #64748b !important; }
    }

    /* Result Card - Optimized for all screens */
    .result-card {
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: 12px;
        padding: clamp(1rem, 5vw, 1.5rem);
        margin: 1rem 0;
        width: 100%;
    }

    .step-header {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 0.75rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid var(--card-border);
    }

    .step-number {
        background: linear-gradient(135deg, #6366f1, #a855f7);
        color: white;
        width: 24px;
        height: 24px;
        border-radius: 50%;
        display: flex;
        flex-shrink: 0;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 12px;
    }

    .step-title {
        font-size: clamp(0.95rem, 5vw, 1.1rem);
        font-weight: 600;
        color: var(--text-main);
    }
    @media (prefers-color-scheme: light) {
        .step-title { color: #1e293b !important; }
    }

    .content-box {
        background: rgba(99, 102, 241, 0.05);
        border-left: 3px solid #6366f1;
        padding: 0.75rem 1rem;
        border-radius: 0 8px 8px 0;
        margin: 0.75rem 0;
        font-size: 0.95rem;
    }

    .rationale-text {
        font-style: italic;
        font-size: 0.85rem;
        line-height: 1.5;
        color: var(--text-sub);
    }
    @media (prefers-color-scheme: light) {
        .rationale-text { color: #475569 !important; }
    }

    /* Sidebar and Controls */
    .sidebar-title {
        font-size: clamp(1rem, 5vw, 1.2rem);
        font-weight: 700;
        background: linear-gradient(135deg, #6366f1, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    
    .config-label {
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 0.3rem;
        margin-top: 0.75rem;
        color: var(--text-main);
    }
    @media (prefers-color-scheme: light) {
        .config-label { color: #334155 !important; }
    }
    
    /* Button and Inputs */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1, #a855f7) !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
        width: 100% !important;
        font-size: 0.9rem !important;
    }

    /* Streamlit UI Tweaks */
    .streamlit-expanderHeader {
        color: var(--text-main) !important;
        font-size: 0.9rem !important;
    }
    
    @media (prefers-color-scheme: light) {
        .streamlit-expanderHeader { color: #1e293b !important; }
        .streamlit-expanderContent { color: #334155 !important; }
    }

    /* Fix Emoji Colors - Prevent gradient/transparency */
    .native-emoji {
        -webkit-text-fill-color: initial !important;
        background: none !important;
        -webkit-background-clip: initial !important;
        background-clip: initial !important;
        filter: none !important;
    }

    /* Tablet/Landscape Adjustments */
    @media (min-width: 768px) {
        .main .block-container {
            padding-left: 3rem;
            padding-right: 3rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# Sidebar Configuration - HYBRID ENGINE
# =============================================================================
with st.sidebar:
    st.markdown('<p class="sidebar-title"><span class="native-emoji">⚙️</span> Hybrid Engine</p>', unsafe_allow_html=True)
    
    # Brain Selection (Provider)
    st.markdown('<p class="config-label"><span class="native-emoji">🧠</span> Select Brain</p>', unsafe_allow_html=True)
    provider = st.selectbox(
        "Provider",
        ["Ollama (Free/Local)", "DeepSeek", "OpenAI"],
        index=0,  # Default to Ollama (FREE)
        label_visibility="collapsed"
    )
    
    # Map display name to provider key
    provider_map = {
        "Ollama (Free/Local)": "ollama",
        "DeepSeek": "deepseek",
        "OpenAI": "openai"
    }
    provider_key = provider_map[provider]
    
    # Get available models for selected provider
    available_models = ModelFactory.get_available_models(provider_key)
    
    st.markdown('<p class="config-label">Model</p>', unsafe_allow_html=True)
    model = st.selectbox(
        "Model",
        available_models,
        label_visibility="collapsed"
    )
    
    # Conditional: Show API Key only for paid providers
    api_key = None
    if ModelFactory.requires_api_key(provider_key):
        st.markdown('<p class="config-label">🔑 API Key</p>', unsafe_allow_html=True)
        api_key = st.text_input(
            "API Key",
            type="password",
            placeholder="sk-... or deepseek-...",
            label_visibility="collapsed"
        )
    else:
        pass  # No status message for Ollama
    
    st.markdown("---")
    
    # Architecture Mode
    st.markdown('<p class="config-label">🏗️ Architect Mode</p>', unsafe_allow_html=True)
    mode = st.selectbox(
        "Mode",
        ["Standard RAG", "Multi-Hop Reasoning", "Autonomous ReAct Agent", "Self-Reflecting Architect"],
        label_visibility="collapsed"
    )
    
    # Retrieval Settings
    st.markdown('<p class="config-label">🔍 Retrieval Mode</p>', unsafe_allow_html=True)
    retrieval_mode = st.selectbox(
        "Retrieval Mode",
        ["📚 Local Knowledge Base (Stable)", "🌐 ColBERTv2 Wikipedia (Remote)"],
        index=0,  # Default to Local Knowledge Base (always works)
        label_visibility="collapsed"
    )
    
    # Only show URL input if ColBERT is selected
    retriever_url = Config.COLBERT_URL
    if "ColBERTv2" in retrieval_mode:
        st.markdown('<p class="config-label">📡 ColBERT Endpoint</p>', unsafe_allow_html=True)
        retriever_url = st.text_input(
            "Retriever URL",
            value=Config.COLBERT_URL,
            label_visibility="collapsed"
        )
        st.warning("⚠️ Remote server may be unstable. Use 'Local Knowledge Base' for reliability.")
    
    st.markdown('<p class="config-label">📊 Top-K Results</p>', unsafe_allow_html=True)
    top_k = st.slider("Top-K", 1, 10, 3, label_visibility="collapsed")
    
    # Configuration Status
    st.markdown("---")
    if provider_key == "ollama":
        st.success("🟢 Ready (Free Mode)")
    elif api_key:
        st.success("🟢 Ready (Cloud Mode)")
    else:
        st.warning("⚠️ Enter API Key to continue")

# =============================================================================
# Configure DSPy (Thread-safe approach with change detection)
# =============================================================================

# Map UI choice to retriever type
retriever_type = "mock" if "Local Knowledge Base" in retrieval_mode else "colbert"

# Create a config hash to detect changes
config_hash = f"{provider_key}:{model}:{retrieval_mode}:{retriever_url}"

# Initialize session state
if 'dspy_configured' not in st.session_state:
    st.session_state.dspy_configured = False
    st.session_state.config_error = None
    st.session_state.config_hash = None

# Reconfigure if settings changed OR not configured yet
if st.session_state.config_hash != config_hash:
    st.session_state.dspy_configured = False

# Prepare and configure DSPy
if (provider_key == "ollama" or api_key) and not st.session_state.dspy_configured:
    try:
        lm = ModelFactory.get_model(provider_key, model, api_key)
        rm = ModelFactory.get_retriever(retriever_type, retriever_url, top_k)
        dspy.settings.configure(lm=lm, rm=rm)
        st.session_state.dspy_configured = True
        st.session_state.config_error = None
        st.session_state.config_hash = config_hash
    except RuntimeError as e:
        # If threading error, check if we can just update the hash
        if "thread that initially configured" in str(e):
            st.session_state.dspy_configured = True
            st.session_state.config_error = None
        else:
            st.session_state.config_error = str(e)
    except Exception as e:
        st.session_state.config_error = str(e)

# =============================================================================
# Hero Section
# =============================================================================
st.markdown('<h1 class="hero-title"><span class="native-emoji">🧠</span> AURA Research Architect</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Self-Evolving Cognitive Pipeline for Research Synthesis</p>', unsafe_allow_html=True)

# (Pipeline visualization removed for cleaner UI)

# =============================================================================
# Input Section
# =============================================================================
st.markdown("---")

query = st.text_area(
    "Research Goal",
    height=120,
    placeholder="e.g., What are the key limitations of Federated Learning in medical imaging, and how do privacy-preserving techniques like Differential Privacy address them?"
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    run_button = st.button("🚀 Evolve & Research", use_container_width=True)

# =============================================================================
# Execution & Results
# =============================================================================
if run_button:
    # Validation
    if provider_key != "ollama" and not api_key:
        st.error("⚠️ Please provide an API key for cloud providers.")
    elif not query:
        st.warning("Please enter a research goal.")
    elif hasattr(st.session_state, 'config_error') and st.session_state.config_error:
        st.error(f"⚠️ Configuration Error: {st.session_state.config_error}")
    elif not st.session_state.get('dspy_configured', False):
        st.error("⚠️ DSPy not configured. Please check your settings.")
    else:
        with st.spinner("🧠 Cognitive pipeline processing..."):
            try:
                # DSPy is already configured at module level
                # Select architecture based on mode
                if mode == "Standard RAG":
                    aura = AuraArchitect(k=top_k)
                    pred = aura(research_goal=query)
                    
                    # Display Results
                    st.markdown("---")
                    
                    # Step 1: Query Generation
                    st.markdown("""
                    <div class="glass-card">
                        <div class="glass-card-title">🔍 Step 1: Query Generation</div>
                    </div>
                    """, unsafe_allow_html=True)
                    with st.expander("View Reasoning", expanded=False):
                        st.write(pred.query_rationale)
                    st.info(f"**Generated Query:** {pred.search_query}")
                    
                    # Step 2: Retrieved Context
                    st.markdown("""
                    <div class="glass-card">
                        <div class="glass-card-title">📚 Step 2: Retrieved Context</div>
                    </div>
                    """, unsafe_allow_html=True)
                    for i, passage in enumerate(pred.context[:top_k]):
                        with st.expander(f"Passage {i+1}", expanded=False):
                            st.write(passage)
                    
                    # Step 3: Synthesized Insight
                    st.markdown("""
                    <div class="glass-card">
                        <div class="glass-card-title">💡 Step 3: Synthesized Insight</div>
                    </div>
                    """, unsafe_allow_html=True)
                    with st.expander("View Reasoning", expanded=False):
                        st.write(pred.synthesis_rationale)
                    st.success(pred.structured_insight)
                    
                elif mode == "Multi-Hop Reasoning":
                    aura = AuraMultiHop(max_hops=2, k=top_k)
                    pred = aura(question=query)
                    
                    st.markdown("---")
                    st.markdown("""
                    <div class="glass-card">
                        <div class="glass-card-title">🔄 Multi-Hop Context (2 hops)</div>
                    </div>
                    """, unsafe_allow_html=True)
                    for i, passage in enumerate(pred.context):
                        with st.expander(f"Hop Result {i+1}", expanded=False):
                            st.write(passage)
                    
                    st.markdown("""
                    <div class="glass-card">
                        <div class="glass-card-title">💡 Final Answer</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.success(pred.answer)
                    
                elif mode == "Autonomous ReAct Agent":
                    aura = AuraAgent()
                    pred = aura(question=query)
                    
                    st.markdown("---")
                    st.markdown("""
                    <div class="glass-card">
                        <div class="glass-card-title">🤖 Agent Answer</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.success(pred.answer)
                    st.info("The agent dynamically used tools (retrieval, calculator) to solve this problem.")
                    
                elif mode == "Self-Reflecting Architect":
                    aura = AuraArchitect(k=top_k)
                    aura.synthesize = AuraReflector(n=3)
                    pred = aura(research_goal=query)
                    
                    st.markdown("---")
                    st.markdown("""
                    <div class="glass-card">
                        <div class="glass-card-title">🪞 Reflected Insight (Best of 3)</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.success(pred.structured_insight)
                    st.info("This insight was selected from 3 candidate generations using a critic model.")
                    
            except Exception as e:
                st.error(f"❌ Pipeline Error: {str(e)}")

