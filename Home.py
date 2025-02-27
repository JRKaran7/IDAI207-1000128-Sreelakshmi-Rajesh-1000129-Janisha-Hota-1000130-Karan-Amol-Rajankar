import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title="Travel Advisor Dashboard", layout="wide")
    
    # Load Logo (Optional)
    logo_path = "Dataset and Database/logo.png"  # Change this to your actual logo file path
    try:
        logo = Image.open(logo_path)
        st.sidebar.image(logo, caption="Travel Advisor", use_container_width=True)
    except:
        st.sidebar.write("No logo found. Add 'logo.png' in the folder.")

    # Load Dashboard Image
    image_path = "Dataset and Database/Dashboard.pdf"  # Change this to your actual image path
    try:
        dashboard_image = Image.open(image_path)
        st.image(dashboard_image, caption="Dashboard Overview", use_container_width=True)
    except:
        st.write("⚠️ Dashboard image not found. Please upload 'dashboard_image.png'.")

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
