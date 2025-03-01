# Year 2 CRS AI Capstone Project 2024 – 25
# Scenario 1 - AI-Driven Gamified Travel Advisor
# Project Name: - Eastern Trails
# Contributors: - Karan Amol Rajankar, Janisha Hota, Sreelakshmi Rajesh

### Introduction
"Travel makes one modest. You see what a tiny place you occupy in the world." – Gustave Flaubert <br> 
India's northeastern states are a treasure trove of culture, landscapes, and traditions that remain relatively unexplored. With diverse communities, breathtaking scenery, and rich heritage, the Northeast offers travelers an unparalleled experience. However, many tourists hesitate due to a lack of reliable travel information and cultural insights.

### Problem Statement
• **Low Awareness & Misconceptions** – Over 65% of Indian travelers are unaware of the diverse attractions in the Northeast, often associating the region only with hill stations like Shillong or Kaziranga, while missing out on lesser-known cultural gems (India Tourism Survey, 2023). <br>
• **Lack of Reliable Travel Information** – More than 70% of potential visitors struggle to find well-organized itineraries, accommodation recommendations, and cultural insights tailored to the Northeast, making trip planning difficult (TripAdvisor India Report, 2023). 
• **Limited Food & Cultural Familiarity** – Over 55% of domestic tourists are hesitant about visiting due to unfamiliarity with local cuisine and customs, fearing they may not find comfortable dining options or cultural guidance (Indian Travel Trends Report, 2023).
• **Seasonal Travel Uncertainty** – The Northeast’s weather varies drastically, and over 60% of travelers find it hard to determine the best time to visit each state, leading to trip cancellations or missed seasonal events like Hornbill Festival or Ziro Music Festival (India Holiday Report, 2022).
• **Transportation Challenges for Tourists** – Around 60% of travelers find it difficult to navigate within the Northeast due to limited public transport options, irregular taxi services, and lack of online booking platforms, making intra-state travel inconvenient (TravelEase India Report, 2023).

### Goal
To bridge this gap, this project aims to create a dedicated travel advisory app for India's northeastern states, offering curated travel recommendations, real-time safety updates, and culturally immersive experiences to promote tourism while ensuring traveler confidence and convenience.

### Objectives
•	Provide authentic, well-researched travel guides for all northeastern states.
•	Integrate real-time safety, weather, and accessibility updates.
•	Highlight the region’s cultural diversity, festivals, and heritage.
•	Offer budget-friendly itinerary planning based on user preferences.

## Journey Map
https://www.canva.com/design/DAGW1mX-TTs/X3iOPZVZzdJyepY2yM__LA/edit?utm_content=DAGW1mX-TTs&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## User Personas
https://www.canva.com/design/DAGVmqOXij0/1wNJU42RPvoJ3c6nf3iqtQ/edit?utm_content=DAGVmqOXij0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Scamper
https://www.canva.com/design/DAGcRi7_t1w/ZkmcyiZYx3yb4tftTQhUNw/edit?utm_content=DAGcRi7_t1w&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Napkin Pitch
https://www.canva.com/design/DAGbk58W9DY/T9uH6A88__T53x7Kq5tAhg/edit

## Features
- **Travel Itinerary:** Create and customize detailed travel itineraries based on user preferences, travel history, and trip duration. Users can choose from AI-suggested plans or manually add locations, accommodations, and activities. The itinerary dynamically adjusts based on weather conditions, local events, and travel disruptions.
- **Chatbot:** Receive AI-powered travel recommendations and instant answers to common travel-related queries. The chatbot provides real-time assistance for itinerary modifications, language translations, emergency contacts, and booking suggestions, ensuring a seamless travel experience.
- **Trivia:** Engage with interactive quizzes that test and expand your knowledge of NorthEast India. Questions are curated based on history, folklore, geography, and cultural traditions, offering an educational and fun way to explore the region. Earn points, unlock rewards, and challenge friends to see who knows the most!
- **Weather:** Get real-time weather updates for various travel destinations, ensuring that your trip is well-planned. The app integrates live forecasting APIs to provide temperature, precipitation, and climate alerts, helping travelers prepare for different weather conditions before and during their journey.
- **Tourist Guide:** Discover must-visit attractions and hidden gems through curated travel guides. These guides include historical backgrounds, best visiting times, insider tips, and local recommendations. Users can also explore offbeat locations that aren't commonly found in mainstream travel lists.
- **Souvenirs:** Explore and shop for authentic regional souvenirs directly through the app. Discover handcrafted items, cultural artifacts, and specialty products from local artisans across NorthEast India. Users can also earn digital collectibles and virtual travel badges as part of their journey.
- **Group Planning(only Frontend):** Coordinate and plan group trips effortlessly with friends and family. The feature allows shared itinerary creation, collaborative decision-making, and real-time updates on group activities. Users can also split costs, set reminders, and vote on destinations and accommodations.
- **Blog:** Read and share travel stories, tips, and guides from experienced travelers. Whether it’s adventure tales, budget travel hacks, or cultural deep-dives, this feature creates a community-driven platform where users can exchange insights and recommendations.
Game: Enjoy interactive travel games designed to make planning fun and engaging. These games incorporate elements of adventure, exploration, and trivia, encouraging users to learn more about their destinations while competing for rewards.
- **AI-Driven Personalized Recommendations:** Uses collaborative filtering and content-based recommendation algorithms to suggest destinations based on user preferences, travel history, and real-time trends. Features dynamic itinerary generation with adaptive route optimization, considering weather conditions, cultural events, and user interests.
- **Virtual Trekking:** A simple trekking game where players "explore" virtual landscapes of the northeastern states using hand gestures or keyboard keys.

## Technologies Used

1. Python
2. Streamlit
3. SQLite
4. Pandas
5. NumPy
6. Scikit-learn
7. Pygame
8. OpenCV (CV2)
9. Datetime
10.requests
11.PIL (Pillow)
12. HTML
13. CSS

## Collaborative Vs. Content-Based Filtering
This system is using content-based filtering.
In content-based filtering, recommendations are based on the features or attributes of the items (in this case, travel packages) and the user's preferences. Here’s why:
**User Input-Based Recommendations:** The system asks the user for their preferences (e.g., weather, budget level, popularity, etc.), and it then uses these preferences to make predictions about the most appropriate travel package.
**Feature Matching:** The system encodes user preferences and matches them with features of travel packages stored in the dataset, such as "Weather", "Budget Level", "Popularity", etc. The package is recommended based on these feature similarities, rather than relying on other users' behavior (which would be typical in collaborative filtering).

## Rewards-System
Badges: Awarded for milestones like visiting landmarks or eco-friendly actions.
Virtual Souvenirs: Collectibles for explored destinations, or points earned based on bookings and interactive features
Points System: Redeem points for discounts, travel coupons, or premium app features.

## Data Preprocessing
- Our Dataset contains entries with information for each on State, Weather, Budget Level, Budget (INR), Transportation Options, Food , Hotels , Famous Places to Visit , Activities, Popularity, Reviews, Season, Language ,Safety ,Family-Friendly, Cultural Highlights
- It has 10,000 total entries.
- Class Imbalance: Applied SMOTE (Synthetic Minority Oversampling Technique) to handle class imbalance effectively.
- Scaling: Standardized numerical features to normalize their range and improve model training stability.
- Encoding: label encoded categorical variables, such as destination type and travel preferences, for machine interpretability.

**Usage Instructions**

Upon launching the app, the home page will display a header with the Eastern Trails logo and title. A subtitle briefly explains the purpose of the app. The main section displays feature cards (such as Travel Itinerary, Chatbot, Trivia, etc.) arranged in a grid. Click any card to navigate to that feature's dedicated page. Each feature page provides detailed information and interactive tools for planning your trip. Enjoy exploring travel options and planning your adventure through NorthEast India!

**Contribution Guidelines**

1. Contributions are welcome! To contribute:
2. Fork the Repository.
3. Create a New Branch for your feature or bug fix
4. git checkout -b feature/your-feature-name
5. Commit Your Changes with clear and descriptive commit messages.
6. Push Your Branch to your fork
7. Open a Pull Request on GitHub describing your changes.
8. Please follow the existing code style and structure.

**Acknowledgments**

Streamlit: For providing an easy-to-use framework for building interactive web applications.
OpenCV & NumPy: For their powerful image processing and numerical computation capabilities.
Gemini API: For offering an affordable alternative to OpenAI’s API for chatbot functionality.
Community and Documentation: Thanks to the open-source community for tutorials, forums, and resources that helped shape this project.

**Screenshots / Demos**

