import streamlit as st
from datetime import datetime

def render_navbar():
    """Render top navigation bar with interactive elements"""
    
    # Custom CSS (same as above)
    st.markdown("""
        <style>
        /* Same CSS as before */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.75rem 2rem;
            background-color: transparent;
            border-bottom: 1px solid #e5e7eb;
            margin-bottom: 1rem;
        }
        
        .nav-left {
            display: flex;
            gap: 2rem;
            align-items: center;
        }
        
        .nav-item {
            color: #6b7280;
            font-size: 0.95rem;
            text-decoration: none;
            cursor: pointer;
            transition: color 0.2s;
        }
        
        .nav-item:hover {
            color: #1a1a1a;
        }
        
        .nav-item.active {
            color: #1a1a1a;
            font-weight: 500;
        }
        
        .nav-item.active::before {
            content: "• ";
            color: #8b7bef;
        }
        
        .nav-right {
            display: flex;
            gap: 1.5rem;
            align-items: center;
        }
        
        .nav-time {
            color: #6b7280;
            font-size: 0.9rem;
        }
        
        .nav-icon {
            color: #6b7280;
            font-size: 1.2rem;
            cursor: pointer;
            transition: color 0.2s;
        }
        
        .nav-icon:hover {
            color: #1a1a1a;
        }
        
        .dropdown-arrow {
            font-size: 0.7rem;
            margin-left: 0.3rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Get current time
    current_time = datetime.now().strftime("%b %d, %I:%M%p").replace("AM", "am").replace("PM", "pm")
    
    # Create columns for navbar
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Left navigation items
        nav_cols = st.columns(5)
        with nav_cols[0]:
            st.markdown('<span class="nav-item active">• Home</span>', unsafe_allow_html=True)
        with nav_cols[1]:
            st.markdown('<span class="nav-item">Smart View</span>', unsafe_allow_html=True)
        with nav_cols[2]:
            st.markdown('<span class="nav-item">Calendar ▼</span>', unsafe_allow_html=True)
        with nav_cols[3]:
            st.markdown('<span class="nav-item">Online Tools ▼</span>', unsafe_allow_html=True)
        with nav_cols[4]:
            st.markdown('<span class="nav-item">End of Day</span>', unsafe_allow_html=True)
    
    with col2:
        # Right side - time and icons
        right_cols = st.columns([2, 1, 1, 1, 1])
        with right_cols[0]:
            st.markdown(f'<span class="nav-time">{current_time}</span>', unsafe_allow_html=True)
        with right_cols[1]:
            st.markdown('<span class="nav-icon">⚙️</span>', unsafe_allow_html=True)
        with right_cols[2]:
            st.markdown('<span class="nav-icon">⬇️</span>', unsafe_allow_html=True)
        with right_cols[3]:
            st.markdown('<span class="nav-icon">💬</span>', unsafe_allow_html=True)
        with right_cols[4]:
            st.markdown('<span class="nav-icon">🔔</span>', unsafe_allow_html=True)
    
    # Add horizontal line
    st.markdown("<hr style='margin: 0; border: 1px solid #e5e7eb;'>", unsafe_allow_html=True)
