import streamlit as st
from streamlit_extras.let_it_rain import rain

# --- 1. THEME & SETTINGS ---
st.set_page_config(page_title="Our Sunflower Universe", page_icon="🌻", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
        color: #FFD700;
    }
    h1, h2, h3 {
        color: #FFD700 !important;
        font-family: 'Trebuchet MS', sans-serif;
        text-shadow: 2px 2px #E94560;
    }
    .stCheckbox { color: white !important; }
    .stButton>button {
        background-color: #E94560;
        color: white;
        border-radius: 20px;
        border: 2px solid #FFD700;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SUBTLE SUNFLOWER RAIN ---
rain(emoji="🌻", falling_speed=10, animation_length="infinite")

# --- 3. HERO SECTION & SOUNDTRACK ---
st.title("🌻 Our Sunflower Universe")
st.write("### You're the Sunflower to my Spider-Verse")

# Spotify Embed for our song
st.markdown('<iframe src="https://open.spotify.com/embed/track/3G7tRCv4UsgtwDCC7sq1oV" width="100%" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>', unsafe_allow_html=True)

st.divider()

# --- 4. OUR JOURNEY ---
st.subheader("🏍️ Our Road Trip Adventure")
trip = st.select_slider("How far have we come?", options=['Met', 'First Date', 'Bike Trips', 'Orlando Move', 'The Future'])
st.info(f"Currently at the **{trip}** stage of our multiverse!")

# --- 5. THE SURPRISE ---
st.divider()
if st.button("Click for our Multiverse Surprise"):
    st.balloons()
    # Ensure 'us_cartoon.png' is in your 'Last Sem' folder
    st.image("us_cartoon.png", caption="You, Me, and our NYC Adventure")
    st.success("I love sharing this life with you! Happy Valentine's Day!")