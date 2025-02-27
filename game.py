import streamlit as st
import cv2
import numpy as np
import random
from pose_tracking import detect_leg_movement
from game_logic import VirtualTrekGame
from database import init_db, save_score, get_high_score

# Initialize database
init_db()

# Streamlit Page Configuration
st.set_page_config(page_title="Virtual Trek", layout="centered")

# Initialize session state
if "score" not in st.session_state:
    st.session_state.score = 0
if "max_score" not in st.session_state:
    st.session_state.max_score = get_high_score()
if "coin_x" not in st.session_state:
    st.session_state.coin_x = random.randint(600, 800)
if "game_running" not in st.session_state:
    st.session_state.game_running = True

# Load assets
player = cv2.imread("assets/player.png")
coin_img = cv2.imread("assets/coin.png")
background = cv2.imread("assets/background.jpeg")
ground_img = cv2.imread("assets/ground.png")

# Resize assets
player = cv2.resize(player, (100, 100))
coin_img = cv2.resize(coin_img, (30, 30))
background = cv2.resize(background, (800, 400))
ground_img = cv2.resize(ground_img, (800, 50))

# OpenCV Video Capture
cap = cv2.VideoCapture(1)

# Streamlit Layout
st.title("🏔️ Virtual Trek Game 🏃‍♂️")
st.markdown("Walk in place to collect coins and increase your score!")

# Video Feed
frame_placeholder = st.empty()

# Score Display
score_col, max_score_col = st.columns(2)
with score_col:
    st.subheader(f"Score: {st.session_state.score}")
with max_score_col:
    st.subheader(f"Max Score: {st.session_state.max_score}")

# Game Loop
while st.session_state.game_running:
    ret, frame = cap.read()
    if not ret:
        st.error("Error: Camera feed failed.")
        break

    frame = cv2.flip(frame, 1)  # Flip for mirror effect
    frame = cv2.resize(frame, (800, 400))

    # Detect Leg Movement
    if detect_leg_movement(frame):
        st.session_state.coin_x -= 20  # Move coin left

    # Check if player collects the coin
    if abs(st.session_state.coin_x - 100) < 40:
        st.session_state.score += 10
        if st.session_state.score > st.session_state.max_score:
            st.session_state.max_score = st.session_state.score
        st.session_state.coin_x = random.randint(600, 800)  # Respawn coin

    # If coin moves off-screen, respawn it
    if st.session_state.coin_x < -30:
        st.session_state.coin_x = random.randint(600, 800)

    # Draw Game Frame
    game_frame = background.copy()
    game_frame[350:400, :] = ground_img  # Draw ground
    game_frame[250:350, 100:200] = player  # Draw player
    game_frame[250:280, st.session_state.coin_x:st.session_state.coin_x+30] = coin_img  # Draw coin

    # Convert to RGB for Streamlit
    game_frame = cv2.cvtColor(game_frame, cv2.COLOR_BGR2RGB)

    # Update Frame
    frame_placeholder.image(game_frame, channels="RGB")

    # Update Score Display
    score_col.subheader(f"Score: {st.session_state.score}")
    max_score_col.subheader(f"Max Score: {st.session_state.max_score}")

# Save Score Before Exiting
save_score(st.session_state.score)
cap.release()
cv2.destroyAllWindows()
st.session_state.game_running = False
