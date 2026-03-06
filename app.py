import streamlit as st
import requests
import streamlit as st

st.set_page_config(
    page_title="Jelstima Smart Gate",
    page_icon="🏠", # You can use any emoji here like ⚡, 🔓, or 🏰
)

import streamlit as st

# 1. Keep your page config at the top
st.set_page_config(page_title="Jelstima Smart Gate", page_icon="🏠")

# 2. Add this CSS block to hide the GitHub icon, Profile pic, and Footer
hide_style = """
    <style>
    /* Hides the top-right GitHub link and profile icon */
    header {visibility: hidden;}
    
    /* Hides the 'Made with Streamlit' footer at the bottom */
    footer {visibility: hidden;}
    
    /* Optional: Hides the red decoration bar at the top */
    div[data-testid="stDecoration"] {
        display: none;
    }
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# Your app content starts here
st.title("Main Gate Controller")

# --- CONFIG ---
# Since you're testing, this IP probably won't reach a real Shelly yet.
# We will add a "Mock Mode" so you can see it work without the hardware.
SHELLY_IP = "192.168.1.50" 

st.set_page_config(page_title="Gate Remote", page_icon="🚪")

# Modern Styling
st.markdown("""
    <style>
    .stButton > button {
        width: 200%;
        height: 100px;
        font-size: 25px;
        border-radius: 15px;
        background-color: #007BFF;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Otvaranje Ograde")

if st.button("🔓 Otvori Ogradu"):
    # For testing without a real Shelly, we wrap this in a try/except
    try:
        url = f"http://{SHELLY_IP}/relay/0?turn=on&timer=1"
        # In a real test, this would send the command
        # response = requests.get(url, timeout=2) 
        
        # MOCK SUCCESS FOR TESTING:
        st.success("Otvaranje ograde..")
        st.balloons() # Just for fun to celebrate your first button!
        
    except Exception as e:
        st.error(f"Connection Failed: {e}")
