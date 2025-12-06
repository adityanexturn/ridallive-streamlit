import streamlit as st
from utils.openai_handler import OpenAIHandler
from utils.session_manager import add_message, save_conversation

def render_chat_interface():
    """Render the chat interface with message history"""
    
    # Display all messages in the conversation
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    prompt = st.chat_input("Ask anything", key="chat_input")
    
    return prompt

def process_user_input(prompt):
    """Process user input and get AI response"""
    
    # Add user message to chat
    add_message("user", prompt)
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response with streaming
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Initialize OpenAI handler
        openai_handler = OpenAIHandler()
        
        # Get streaming response
        for chunk in openai_handler.get_streaming_response(st.session_state.messages):
            full_response += chunk
            message_placeholder.markdown(full_response + "▌")
        
        # Display final response
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat
    add_message("assistant", full_response)
    
    # Save conversation if it's the first exchange
    if len(st.session_state.messages) == 2:
        save_conversation()
