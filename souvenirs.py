import streamlit as st
from PIL import Image
import os

# Initialize session state for points
if "points" not in st.session_state:
    st.session_state.points = 5000  # Starting points
if "purchased_badges" not in st.session_state:
    st.session_state.purchased_badges = set()

# Badge data
badges = [
    {"name": "Meghalaya", "image": "Meghalaya Badge.png"},
    {"name": "Manipur", "image": "Manipur Badge.png"},
    {"name": "Nagaland", "image": "Nagaland Badge.png"},
    {"name": "Arunachal Pradesh", "image": "Arunachal Pradesh Badge.png"},
    {"name": "Assam", "image": "Assam Badge.png"},
    {"name": "Tripura", "image": "Tripura Badge.png"},
    {"name": "Mizoram", "image": "Mizoram Badge.png"},
]

badge_price = 2000  # Cost per badge

st.title("🎖️ Souvenir Shop")
st.markdown("### Collect badges and spend your points!")

# Display points
st.subheader(f"💰 Points: {st.session_state.points}")

# Layout for two badges per row
col1, col2 = st.columns(2)

for index, badge in enumerate(badges):
    col = col1 if index % 2 == 0 else col2  # Alternate between columns

    # Load image
    image_path = f"Badges/{badge["image"]}"
    if os.path.exists(image_path):
        img = Image.open(image_path)
        img = img.resize((120, 120))
        col.image(img, caption=badge["name"], use_container_width=True)
    else:
        col.warning(f"Image not found: {image_path}")

    # Purchase button
    if badge["name"] not in st.session_state.purchased_badges:
        if col.button(f"Buy ({badge_price} pts)", key=badge["name"]):
            if st.session_state.points >= badge_price:
                st.session_state.points -= badge_price
                st.session_state.purchased_badges.add(badge["name"])
                st.success(f"✅ Purchased {badge['name']} Badge!")
            else:
                st.error("❌ Not enough points!")

# Completion Message
if len(st.session_state.purchased_badges) == len(badges):
    st.success("🏆 Congratulations! You are The Seven Sister Champion!")
