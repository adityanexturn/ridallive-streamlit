import streamlit as st

def load_css(file_path=None):
    """Load CSS - inline version if file not found"""
    css = """
    <style>
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Main content */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 0rem;
        max-width: 100%;
    }

    /* Sidebar styling - uses theme colors */
    [data-testid="stSidebar"] {
        padding-top: 1rem;
    }

    /* Welcome container */
    .welcome-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 45vh;
        text-align: center;
    }

    .welcome-title {
        font-size: 3.5rem;
        font-weight: 600;
        margin-bottom: 2.5rem;
        letter-spacing: -0.02em;
    }

    /* Chat input styling */
    .stChatInput > div {
        border-radius: 24px;
    }

    /* Suggested questions */
    .suggested-section {
        margin-top: 2.5rem;
        text-align: center;
    }

    .suggested-label {
        font-size: 0.95rem;
        margin-bottom: 1.5rem;
        opacity: 0.7;
    }

    /* Secondary button styling for questions */
    .stButton button[kind="secondary"] {
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        text-align: left;
        font-weight: 400;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }

    /* Empty state */
    .empty-state {
        text-align: center;
        padding: 3rem 1rem;
    }

    .empty-state-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        opacity: 0.5;
    }

    .empty-state-text {
        opacity: 0.6;
    }

    .empty-state-action {
        font-weight: 600;
    }

    .conv-count {
        font-size: 0.9rem;
        margin: 1rem 0;
        opacity: 0.7;
    }

    .footer-text {
        font-size: 0.85rem;
        font-style: italic;
        margin-top: 2rem;
        opacity: 0.6;
    }

    /* Chat messages */
    [data-testid="stChatMessage"] {
        border-radius: 8px;
        padding: 1rem;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def truncate_text(text, max_length=50):
    """Truncate text to specified length"""
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text
