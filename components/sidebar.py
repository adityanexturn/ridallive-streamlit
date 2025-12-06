import streamlit as st
from utils.session_manager import clear_current_chat, get_conversation_count, load_conversation

def render_sidebar():
    """Render the sidebar with chat history"""
    with st.sidebar:
        # Header with Chat History and New button
        col1, col2 = st.columns([2.5, 1])
        with col1:
            st.markdown("## Chat History")
        with col2:
            if st.button("➕ New", key="new_chat_btn", use_container_width=True):
                clear_current_chat()
                st.rerun()
        
        st.markdown("---")
        
        # Display conversation count
        conv_count = get_conversation_count()
        st.markdown(f'<p class="conv-count">{conv_count} conversations</p>', unsafe_allow_html=True)
        
        # Empty state or conversation list
        if conv_count == 0:
            st.markdown("""
                <div class="empty-state">
                    <div class="empty-state-icon">➕</div>
                    <p class="empty-state-text">No conversations yet</p>
                    <p class="empty-state-action">Start your first chat</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            # Display saved conversations
            for idx, conv in enumerate(st.session_state.conversations):
                if st.button(f"💬 {conv['title']}", key=f"conv_{idx}", use_container_width=True):
                    load_conversation(idx)
                    st.rerun()
        
        # Footer text
        st.markdown("---")
        st.markdown(
            '<p class="footer-text">Your conversations are saved locally</p>', 
            unsafe_allow_html=True
        )
