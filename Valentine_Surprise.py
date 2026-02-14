import streamlit as st
import os
from PIL import Image, ImageOps
from streamlit_snowfall import snowfall

# 1. PAGE CONFIG
st.set_page_config(page_title="Our Sunflower Universe", page_icon="🌻", layout="wide")

# 2. GLITTER EFFECT
snowfall(flake_color=["#FFD700", "#FFFFFF", "#FFBE0B"], num_flakes=150, speed=2)

# 3. CUSTOM THEME (Original Size Fix)
st.markdown("""
    <style>
    .stApp { background: linear-gradient(180deg, #090A0F 0%, #1a1a2e 100%) !important; color: #FFD700; }
    h1, h2, h3 { color: #FFD700 !important; text-shadow: 2px 2px #E94560; }
    
    /* ORIGINAL SIZE: Natural height, no cropping */
    [data-testid="stHorizontalBlock"] .stImage img {
        width: 100% !important;
        height: auto !important; /* Natural height */
        object-fit: contain !important; /* Shows full photo */
        border-radius: 15px;
        border: 2px solid #E94560;
        transition: transform 0.3s ease;
        margin-bottom: 20px;
    }
    .stImage img:hover { transform: scale(1.05); border: 2px solid #FFD700; }
    .stButton>button { background-color: #E94560; color: white; border-radius: 20px; border: 2px solid #FFD700; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# 4. HEADER & AUDIO
st.title("🌻 Our Sunflower Universe")
st.write("### You're the Sunflower to my Spider-Verse")

# Note: Ensure you update this with your Direct Google Drive link if song.mp4 doesn't play
audio_path = "song.mp4"
if os.path.exists(audio_path):
    st.audio(audio_path, format='audio/mp4')

# 5. ROAD TRIP SLIDER
st.subheader("🏍️ Our Road Trip Adventure")
milestones = ["Met", "First Date", "Gokarna Trip", "Orlando Move", "The Future"]
choice = st.select_slider("Where are we in the Multiverse?", options=milestones, value="Orlando Move")

def fix_image_orientation(image_input):
    try:
        img = Image.open(image_input)
        img = ImageOps.exif_transpose(img)
        return img
    except: return None

# 6. MULTIVERSE ALBUM (Masonry Layout for Original Sizes)
st.markdown("---")
st.header("🎞️ Multiverse Album")

# Finding photos in the main GitHub folder
all_photos = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
all_photos.sort()

if not all_photos:
    st.info("Gathering memories...")
else:
    # Creating 3 vertical columns to let photos stack naturally by height
    col1, col2, col3 = st.columns(3)
    for i, img_path in enumerate(all_photos):
        processed_img = fix_image_orientation(img_path)
        if processed_img:
            if i % 3 == 0:
                col1.image(processed_img, use_container_width=True)
            elif i % 3 == 1:
                col2.image(processed_img, use_container_width=True)
            else:
                col3.image(processed_img, use_container_width=True)

# 7. SURPRISE
st.markdown("---")
if st.button("Click for our Multiverse Surprise ❤️"):
    st.balloons()
    st.success("I love sharing this life with you! Happy Valentine's Day!")
