import streamlit as st
import time

# --- 1. SETTING THE STAGE ---
st.set_page_config(page_title="HBD Dhishyah! 🎀", page_icon="💖")

st.markdown("""
    <style>
    .stApp { background-color: #ffe6f2; }
    
    /* Force text to be deep black and bold */
    h1, h2, h3, p, span, .stMarkdown {
        color: #000000 !important; 
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    
    .stButton>button {
        background-color: #ff4d94;
        color: white !important;
        border-radius: 25px;
        height: 3.5em;
        width: 100%;
        font-weight: bold;
        font-size: 20px;
        border: 3px solid #ff0066;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SESSION STATE (To change content after clicking) ---
if 'celebrate' not in st.session_state:
    st.session_state.celebrate = False

# --- 3. THE UI ---
if not st.session_state.celebrate:
    st.write("# 🎀 I made something special for u, Dhishyah! 🎀")
    st.write("## Do u want to see it?")
    
    # Cute Bubu & Dudu waiting GIF
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueG56Z3R6ZzR4eHhzOHR6ZzR4eHhzOHR6ZzR4eHhzOHR6ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/L4lvBpHWkARu8/giphy.gif")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES! ✅"):
            st.session_state.celebrate = True
            st.rerun()
    with col2:
        if st.button("NO ❌"):
            st.error("Error: This button is just for show. Click YES! 😂")
            time.sleep(0.5)
            st.rerun()

else:
    # --- THE SURPRISE SCREEN ---
    st.balloons()
    st.snow()
    
    st.write("# 🎉 Happy Birthday Loosu! 🤪")
    
    # Happy Birthday Celebration GIF
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDByOXBqam8zemZ2ZzR4eHhzOHR6ZzR4eHhzOHR6ZzR4eHhzOHR6ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/Nm8ZPAGOwZUQM/giphy.gif")
    
    st.write("### 🎂 Official Birthday Report for Dhishyah:")
    st.write("1. **Vibe Check:** 100% Chaos. 🌪️")
    st.write("2. **Brain Cells:** Still loading... ⏳")
    st.write("3. **Icon Status:** Certified Legend. ⭐")
    
    st.info("Congratulations! You are officially one year closer to becoming a crazy cat lady. Enjoy your day, you absolute menace! 🥳")
    
    if st.button("Back to Start 🔄"):
        st.session_state.celebrate = False
        st.rerun()

