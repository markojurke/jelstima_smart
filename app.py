import streamlit as st
import requests

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
