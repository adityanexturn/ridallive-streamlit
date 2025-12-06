import streamlit as st
from datetime import datetime
from streamlit_calendar import calendar as st_calendar

def render_navbar():
    """Render top navigation bar with interactive calendar dropdown"""
    
    # Initialize session state for dropdown
    if "show_calendar" not in st.session_state:
        st.session_state.show_calendar = False
    if "show_tools" not in st.session_state:
        st.session_state.show_tools = False
    
    # Custom CSS for navbar
    st.markdown("""
        <style>
        /* Navbar container */
        .navbar-container {
            padding: 0.75rem 2rem;
            border-bottom: 1px solid rgba(128, 128, 128, 0.2);
            margin-bottom: 1rem;
        }
        
        /* Navigation items styling */
        .stButton > button {
            background-color: transparent !important;
            border: none !important;
            color: inherit !important;
            padding: 0.5rem 0.75rem !important;
            font-size: 0.95rem !important;
            font-weight: 400 !important;
            box-shadow: none !important;
        }
        
        .stButton > button:hover {
            background-color: rgba(128, 128, 128, 0.1) !important;
        }
        
        /* Time display */
        .nav-time {
            font-size: 0.9rem;
            opacity: 0.7;
            padding: 0.5rem;
        }
        
        /* Icon styling */
        .nav-icon {
            font-size: 1.2rem;
            cursor: pointer;
            opacity: 0.7;
            transition: opacity 0.2s;
        }
        
        .nav-icon:hover {
            opacity: 1;
        }
        
        /* Calendar dropdown styling */
        .calendar-dropdown {
            border: 1px solid rgba(128, 128, 128, 0.2);
            border-radius: 8px;
            padding: 1rem;
            margin-top: 0.5rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        /* Active nav item */
        .active-nav {
            font-weight: 600 !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Get current time
    current_time = datetime.now().strftime("%b %d, %I:%M%p").replace("AM", "am").replace("PM", "pm")
    
    # Main navbar container
    with st.container():
        st.markdown('<div class="navbar-container">', unsafe_allow_html=True)
        
        # Create columns for navbar layout
        col1, col_spacer, col2 = st.columns([3, 0.5, 1.5])
        
        with col1:
            # Left navigation items
            nav_cols = st.columns([1, 1.2, 1.2, 1.5, 1.2])
            
            with nav_cols[0]:
                st.markdown('<div class="active-nav">• Home</div>', unsafe_allow_html=True)
            
            with nav_cols[1]:
                if st.button("Smart View", key="smart_view_nav", use_container_width=True):
                    pass  # Add functionality here
            
            with nav_cols[2]:
                if st.button("Calendar ▼", key="calendar_nav", use_container_width=True):
                    st.session_state.show_calendar = not st.session_state.show_calendar
                    st.session_state.show_tools = False  # Close other dropdowns
            
            with nav_cols[3]:
                if st.button("Online Tools ▼", key="tools_nav", use_container_width=True):
                    st.session_state.show_tools = not st.session_state.show_tools
                    st.session_state.show_calendar = False  # Close other dropdowns
            
            with nav_cols[4]:
                if st.button("End of Day", key="end_day_nav", use_container_width=True):
                    pass  # Add functionality here
        
        with col2:
            # Right side - time and icons
            right_cols = st.columns([2, 0.8, 0.8, 0.8, 0.8])
            
            with right_cols[0]:
                st.markdown(f'<div class="nav-time">{current_time}</div>', unsafe_allow_html=True)
            
            with right_cols[1]:
                st.markdown('<div class="nav-icon">⚙️</div>', unsafe_allow_html=True)
            
            with right_cols[2]:
                st.markdown('<div class="nav-icon">⬇️</div>', unsafe_allow_html=True)
            
            with right_cols[3]:
                st.markdown('<div class="nav-icon">💬</div>', unsafe_allow_html=True)
            
            with right_cols[4]:
                st.markdown('<div class="nav-icon">🔔</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Show calendar dropdown if toggled
    if st.session_state.show_calendar:
        with st.container():
            st.markdown('<div class="calendar-dropdown">', unsafe_allow_html=True)
            
            # Calendar configuration
            calendar_options = {
                "editable": True,
                "selectable": True,
                "headerToolbar": {
                    "left": "prev,next today",
                    "center": "title",
                    "right": "dayGridMonth,timeGridWeek,timeGridDay"
                },
                "initialView": "dayGridMonth",
                "initialDate": datetime.now().strftime("%Y-%m-%d"),
                "slotMinTime": "06:00:00",
                "slotMaxTime": "22:00:00",
                "navLinks": True,
                "nowIndicator": True,
            }
            
            # Sample events (you can customize or load from data)
            calendar_events = [
                {
                    "title": "Meeting",
                    "start": datetime.now().strftime("%Y-%m-%d") + "T10:00:00",
                    "end": datetime.now().strftime("%Y-%m-%d") + "T11:00:00",
                    "backgroundColor": "#8b7bef",
                    "borderColor": "#8b7bef"
                },
                {
                    "title": "Lunch Break",
                    "start": datetime.now().strftime("%Y-%m-%d") + "T12:00:00",
                    "end": datetime.now().strftime("%Y-%m-%d") + "T13:00:00",
                    "backgroundColor": "#10b981",
                    "borderColor": "#10b981"
                }
            ]
            
            # Custom CSS for the calendar
            custom_css = """
                .fc-event-past {
                    opacity: 0.8;
                }
                .fc-event-time {
                    font-style: italic;
                }
                .fc-event-title {
                    font-weight: 600;
                }
                .fc-toolbar-title {
                    font-size: 1.5rem !important;
                }
                .fc {
                    font-family: sans-serif;
                }
            """
            
            # Render calendar
            cal_state = st_calendar(
                events=calendar_events,
                options=calendar_options,
                custom_css=custom_css,
                key="navbar_calendar_widget"
            )
            
            # Show selected event details
            if cal_state.get("eventClick"):
                st.info(f"**Event:** {cal_state['eventClick']['event']['title']}")
            
            # Close button
            col_a, col_b, col_c = st.columns([2, 1, 1])
            with col_c:
                if st.button("✕ Close", key="close_calendar", use_container_width=True):
                    st.session_state.show_calendar = False
                    st.rerun()
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Show tools dropdown if toggled
    if st.session_state.show_tools:
        with st.container():
            st.markdown('<div class="calendar-dropdown">', unsafe_allow_html=True)
            st.markdown("### 🔧 Online Tools")
            
            tool_cols = st.columns(2)
            with tool_cols[0]:
                st.markdown("- 📊 Analytics Dashboard")
                st.markdown("- 📈 Reports Generator")
                st.markdown("- 📋 Data Export")
            
            with tool_cols[1]:
                st.markdown("- 🔍 Search Tools")
                st.markdown("- ⚡ Quick Actions")
                st.markdown("- 🎯 Goal Tracker")
            
            if st.button("✕ Close", key="close_tools", use_container_width=True):
                st.session_state.show_tools = False
                st.rerun()
            
            st.markdown('</div>', unsafe_allow_html=True)
