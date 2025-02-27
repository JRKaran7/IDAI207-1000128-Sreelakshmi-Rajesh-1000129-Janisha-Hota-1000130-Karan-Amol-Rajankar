import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title="Travel Advisor Dashboard", layout="wide")
    
    # Load Dashboard Image
    image_path = "dashboard_image.png"  # Change this to your actual image path
    dashboard_image = Image.open(image_path)
    st.image(dashboard_image, caption="Dashboard Overview", use_column_width=True)
    
    st.title("🌍 Travel Advisor Dashboard")
    st.write("Welcome to the ultimate travel companion! Choose an option below to explore features.")
    
    # Navigation Buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Tourist Info 🏕️"):
            st.switch_page("tourist.py")
        if st.button("Souvenirs 🎁"):
            st.switch_page("souvenirs.py")
        if st.button("Chatbot 🤖"):
            st.switch_page("chatbot.py")
    
    with col2:
        if st.button("Travel Itinerary 📅"):
            st.switch_page("travel_itenary.py")
        if st.button("Group Planning 👥"):
            st.switch_page("group_planning.py")
        if st.button("Trivia Quiz ❓"):
            st.switch_page("trivia.py")
    
    with col3:
        if st.button("Weather 🌤️"):
            st.switch_page("weather.py")
        if st.button("News 📰"):
            st.switch_page("news.py")
        if st.button("Blog ✍️"):
            st.switch_page("blog.py")

if __name__ == "__main__":
    main()
