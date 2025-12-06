import streamlit as st

def load_css(file_path):
    """Load CSS from file"""
    try:
        with open(file_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"CSS file not found: {file_path}")

def truncate_text(text, max_length=50):
    """Truncate text to specified length"""
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text
