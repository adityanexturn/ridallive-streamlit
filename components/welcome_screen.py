import streamlit as st

def render_welcome_screen(suggested_questions):
    """Render the welcome screen with suggested questions"""
    
    # Welcome title centered
    st.markdown("""
        <div class="welcome-container">
            <h1 class="welcome-title">Ready when you are.</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # Chat input
    prompt = st.chat_input("Ask anything", key="welcome_chat_input")
    
    # Suggested questions section
    st.markdown("""
        <div class="suggested-section">
            <p class="suggested-label">Suggested questions:</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Center the questions
    col1, col2, col3 = st.columns([0.5, 3, 0.5])
    
    with col2:
        selected_question = None
        for idx, question in enumerate(suggested_questions):
            if st.button(
                question, 
                key=f"suggested_{idx}", 
                use_container_width=True,
                type="secondary"
            ):
                selected_question = question
        
        # Return either typed prompt or selected question
        return prompt if prompt else selected_question
    
    return None
