import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Travel Advisor", page_icon="🌍", layout="wide")

# Header
st.title("🌍 Welcome to Your Travel Advisor")
st.subheader("Plan your perfect trip with ease and fun!")

# Description
st.write("""
Explore personalized recommendations, check the weather, get guided itineraries, chat with our AI bot, play travel trivia, and even shop for souvenirs!
Select a section below to begin your adventure.
""")

# Create buttons/links to each module
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📅 Travel Itinerary"):
        st.switch_page("https://public.tableau.com/views/Instagram_17400490407470/Story1?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link")  # Link to travel itinerary page

    if st.button("🤖 Chat with TravelBot"):
        st.switch_page("pages/chatbot.py")  # Link to chatbot page

    if st.button("🏅 Travel Trivia"):
        st.switch_page("pages/trivia.py")  # Link to trivia page

with col2:
    if st.button("☀️ Check Weather"):
        st.switch_page("pages/weather.py")  # Link to weather page

    if st.button("🗺️ Tourist Guide"):
        st.switch_page("pages/tourist_guide.py")  # Link to tourist guide page

    if st.button("🎁 Souvenirs"):
        st.switch_page("pages/souvenirs.py")  # Link to souvenirs page

with col3:
    if st.button("🌟 Recommendations"):
        st.switch_page("pages/recommendations.py")  # Link to recommendations page

# Optional Footer
st.markdown("---")
st.write("🚀 Developed with ❤️ for travel enthusiasts")

