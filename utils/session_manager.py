import streamlit as st

def initialize_session_state():
    """Initialize all session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "conversations" not in st.session_state:
        st.session_state.conversations = []
    
    if "current_conversation_id" not in st.session_state:
        st.session_state.current_conversation_id = None

def add_message(role, content):
    """Add a message to current conversation"""
    st.session_state.messages.append({
        "role": role,
        "content": content
    })

def clear_current_chat():
    """Clear current chat and start new conversation"""
    st.session_state.messages = []
    st.session_state.current_conversation_id = None

def save_conversation():
    """Save current conversation to history"""
    if len(st.session_state.messages) >= 2:
        first_message = st.session_state.messages[0]["content"]
        title = first_message[:50] + "..." if len(first_message) > 50 else first_message
        
        conversation = {
            "title": title,
            "messages": st.session_state.messages.copy()
        }
        
        st.session_state.conversations.append(conversation)

def load_conversation(index):
    """Load a conversation from history"""
    if 0 <= index < len(st.session_state.conversations):
        st.session_state.messages = st.session_state.conversations[index]["messages"].copy()
        st.session_state.current_conversation_id = index

def get_conversation_count():
    """Get total number of saved conversations"""
    return len(st.session_state.conversations)
