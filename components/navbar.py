import streamlit as st
from datetime import datetime

def render_navbar():
    """Render top navigation bar"""
    
    # Custom CSS for navbar
    st.markdown("""
        <style>
        /* Navbar container */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.75rem 2rem;
            background-color: transparent;
            border-bottom: 1px solid #e5e7eb;
            margin-bottom: 1rem;
        }
        
        /* Left side navigation */
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
        
        /* Right side icons */
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
        
        /* Dropdown indicator */
        .dropdown-arrow {
            font-size: 0.7rem;
            margin-left: 0.3rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Get current time
    current_time = datetime.now().strftime("%b %d, %I:%M%p").replace("AM", "am").replace("PM", "pm")
    
    # Navbar HTML
    navbar_html = f"""
        <div class="navbar">
            <div class="nav-left">
                <span class="nav-item active">Home</span>
                <span class="nav-item">Smart View</span>
                <span class="nav-item">Calendar <span class="dropdown-arrow">▼</span></span>
                <span class="nav-item">Online Tools <span class="dropdown-arrow">▼</span></span>
                <span class="nav-item">End of Day</span>
            </div>
            <div class="nav-right">
                <span class="nav-time">{current_time}</span>
                <span class="nav-icon">⚙️</span>
                <span class="nav-icon">⬇️</span>
                <span class="nav-icon">💬</span>
                <span class="nav-icon">🔔</span>
            </div>
        </div>
    """
    
    st.markdown(navbar_html, unsafe_allow_html=True)
