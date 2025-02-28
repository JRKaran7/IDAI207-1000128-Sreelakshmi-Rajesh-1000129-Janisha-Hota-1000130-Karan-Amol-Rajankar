# Eastern Trails - Travel Advisor App

## Project Title and Description
**Eastern Trails** is an interactive, multi-page travel advisor web application built using Streamlit. The project is designed to help users explore and plan trips across NorthEast India. With an emphasis on local culture and experiences, Eastern Trails provides personalized travel itineraries, AI-powered recommendations, real-time weather updates, engaging trivia quizzes, detailed tourist guides, a curated blog, group planning tools, and interactive travel games.

## Features
- **Travel Itinerary:** Create and customize travel itineraries based on user preferences.
- **Chatbot:** Receive AI-powered travel recommendations and answers to common travel questions.
- **Trivia:** Engage with fun quizzes that test your knowledge of NorthEast India.
- **Weather:** Get real-time weather updates for various travel destinations.
- **Tourist Guide:** Discover must-visit attractions and hidden gems.
- **Souvenirs:** Explore and shop for authentic regional souvenirs.
- **Group Planning:** Coordinate and plan group trips with friends.
- **Blog:** Read and share travel stories, tips, and guides.
- **Game:** Enjoy interactive travel games to make planning fun.

## Technologies Used
- **Programming Language:** Python
- **Framework:** Streamlit
- **Libraries:** 
  - OpenCV (for image and video processing in game features)
  - NumPy (for numerical operations)
  - SQLite3 (for database operations)
- **APIs:** Gemini API (for AI chatbot integration)
- **Other:** Custom CSS for theming and styling

## Installation Instructions
Follow these steps to set up and run the project locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/eastern-trails.git
   cd eastern-trails
Create a Virtual Environment:

bash
Copy
Edit
python -m venv venv
Activate the virtual environment:

On macOS/Linux:
bash
Copy
Edit
source venv/bin/activate
On Windows:
bash
Copy
Edit
venv\Scripts\activate
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Ensure Folder Structure: Your project folder should look like this:

pgsql
Copy
Edit
eastern-trails/
├── Home.py
├── pages/
│   ├── travel_itinerary.py
│   ├── chatbot.py
│   ├── trivia.py
│   ├── weather.py
│   ├── tourist.py
│   ├── souvenirs.py
│   ├── group_planning.py
│   ├── blog.py
│   └── game.py
├── Dataset and Database/
│   ├── eastern_trails_logo.png
│   └── scores.db
├── database.py
├── requirements.txt
└── README.md
Run the Application:

bash
Copy
Edit
streamlit run Home.py
Usage Instructions
Upon launching the app, the home page will display a header with the Eastern Trails logo and title.
A subtitle briefly explains the purpose of the app.
The main section displays feature cards (such as Travel Itinerary, Chatbot, Trivia, etc.) arranged in a grid. Click any card to navigate to that feature's dedicated page.
Each feature page provides detailed information and interactive tools for planning your trip.
Enjoy exploring travel options and planning your adventure through NorthEast India!
Contribution Guidelines
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch for your feature or bug fix:
bash
Copy
Edit
git checkout -b feature/your-feature-name
Commit your changes with clear and descriptive commit messages.
Push your branch to your fork:
bash
Copy
Edit
git push origin feature/your-feature-name
Open a Pull Request on GitHub describing your changes.
Please follow the existing code style and structure.
Acknowledgments
Streamlit: For providing an easy-to-use framework for building interactive web applications.
OpenCV & NumPy: For their powerful image processing and numerical computation capabilities.
Gemini API: For offering an affordable alternative to OpenAI's API for chatbot functionality.
Community and Documentation: Thanks to the open-source community for tutorials, forums, and resources that helped shape this project.
Screenshots / Demos
Home Page

Feature Page Example (Travel Itinerary)

Note: Replace the image paths above with the actual URLs or paths to your screenshots.
