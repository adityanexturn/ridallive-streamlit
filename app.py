import streamlit as st
from utils import initialize_session_state, load_css
from components import render_sidebar, render_welcome_screen, render_chat_interface, process_user_input, render_navbar

# Page configuration
st.set_page_config(
    page_title="Chat Assistant",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_css()

# Initialize session state
initialize_session_state()

# Render top navigation bar with calendar
render_navbar()

# Render sidebar
render_sidebar()

# Define suggested questions
SUGGESTED_QUESTIONS = [
    "How much inventory do I have of the dresses Monarch and Syvil?",
    "How many Monarch and Syvil dresses did I sell in the past year? Give a month by month breakdown.",
    "How many dresses do I need to sell in October to see a $5000 increase in sales revenue? Only consider dresses, not accessories."
]

# Main content area
if len(st.session_state.messages) == 0:
    # Welcome screen (empty state)
    prompt = render_welcome_screen(SUGGESTED_QUESTIONS)
else:
    # Chat interface (active conversation)
    prompt = render_chat_interface()

# Process user input if provided
if prompt:
    process_user_input(prompt)
    st.rerun()
