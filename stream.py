import streamlit as st
import pandas as pd
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load trained model and scaler
model = joblib.load("Models/best_travel_recommender.pkl")
scaler = joblib.load("Models/scaler.pkl")

# Load dataset
df = pd.read_csv("Dataset and Database/Seven_Sisters_Travel_Packages_Cleaned_Encoded.csv")

# Define state mapping
state_mapping = ['Arunachal Pradesh', 'Assam', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Tripura']

# Define categorical mappings
label_mappings = {
    'Weather': ['Chilly', 'Pleasant', 'Rainy', 'Sunny'],
    'Budget Level': ['Low', 'Medium', 'High'],
    'Transportation Options': ['Low', 'Medium', 'High'],
    'Popularity': ['Low', 'Moderate', 'High'],
    'Season': ['Monsoon', 'Summer', 'Winter'],
    'Cultural Highlights': ['Art Exhibitions', 'Festival', 'Local Traditions']
}

# Features used for training
training_features = ['Budget (INR)', 'Reviews', 'Hotel Cost (INR)', 'Food Cost (INR)', 'Season']

# Streamlit UI
st.title("🌍 Travel Recommendation System")
st.markdown("Find the best travel package based on your preferences!")

# Sidebar for user input
st.sidebar.header("🔍 Enter Your Preferences")

# Categorical Inputs
user_input = {}
for feature, options in label_mappings.items():
    user_input[feature] = st.sidebar.selectbox(f"{feature}", options, index=0)

# Numeric Inputs
user_input["Budget (INR)"] = st.sidebar.slider("💰 Budget (₹)", 5000, 50000, 20000, step=1000)
user_input["Food Cost (INR)"] = st.sidebar.slider("🍽 Expected Daily Food Cost (₹)", 500, 5000, 2000, step=100)
user_input["Hotel Cost (INR)"] = st.sidebar.slider("🏨 Expected Per-Night Hotel Cost (₹)", 1000, 20000, 5000, step=500)
user_input["Reviews"] = st.sidebar.slider("⭐ Minimum Rating (1.0 to 5.0)", 1.0, 5.0, 4.0, step=0.1)

# Convert categorical inputs to numerical values
for feature, options in label_mappings.items():
    user_input[feature] = options.index(user_input[feature])

# Convert user input to DataFrame
input_df = pd.DataFrame([user_input])
input_df = input_df[training_features]

# Apply scaling
scaled_input = scaler.transform(input_df)

# Predict recommended travel state
predicted_state_index = model.predict(scaled_input)[0]

# Normalize numeric features
df['Normalized Budget'] = (df['Budget (INR)'] - df['Budget (INR)'].min()) / (df['Budget (INR)'].max() - df['Budget (INR)'].min())
df['Normalized Reviews'] = (df['Reviews'] - df['Reviews'].min()) / (df['Reviews'].max() - df['Reviews'].min())
df['Normalized Food Cost'] = (df['Food Cost (INR)'] - df['Food Cost (INR)'].min()) / (df['Food Cost (INR)'].max() - df['Food Cost (INR)'].min())
df['Normalized Hotel Cost'] = (df['Hotel Cost (INR)'] - df['Hotel Cost (INR)'].min()) / (df['Hotel Cost (INR)'].max() - df['Hotel Cost (INR)'].min())

# Normalize user input
user_normalized = {
    'Normalized Budget': (user_input['Budget (INR)'] - df['Budget (INR)'].min()) / (df['Budget (INR)'].max() - df['Budget (INR)'].min()),
    'Normalized Reviews': (user_input['Reviews'] - df['Reviews'].min()) / (df['Reviews'].max() - df['Reviews'].min()),
    'Normalized Food Cost': (user_input['Food Cost (INR)'] - df['Food Cost (INR)'].min()) / (df['Food Cost (INR)'].max() - df['Food Cost (INR)'].min()),
    'Normalized Hotel Cost': (user_input['Hotel Cost (INR)'] - df['Hotel Cost (INR)'].min()) / (df['Hotel Cost (INR)'].max() - df['Hotel Cost (INR)'].min())
}

# Compute similarity score
df['Season Match'] = (df['Season'] == user_input['Season']).astype(int)
df['Cultural Match'] = (df['Cultural Highlights'] == user_input['Cultural Highlights']).astype(int)

df['Similarity'] = (
    abs(df['Normalized Budget'] - user_normalized['Normalized Budget']) * 0.25 +  
    abs(df['Normalized Reviews'] - user_normalized['Normalized Reviews']) * 0.2 +  
    abs(df['Normalized Food Cost'] - user_normalized['Normalized Food Cost']) * 0.15 +  
    abs(df['Normalized Hotel Cost'] - user_normalized['Normalized Hotel Cost']) * 0.15 +  
    (1 - df['Season Match']) * 0.15 +  
    (1 - df['Cultural Match']) * 0.1  
)

# Filter the dataset to only include results from the predicted state
filtered_df = df[df['State'] == state_mapping[predicted_state_index]]

# If there are no matching states, fall back to the full dataset
if filtered_df.empty:
    filtered_df = df

# Get the best match within the predicted state
recommended_package = filtered_df.nsmallest(1, 'Similarity').to_dict(orient='records')[0]

# Decode categorical values
recommended_package_decoded = {}
for key, value in recommended_package.items():
    if key in label_mappings and isinstance(value, (int, np.integer)):  
        recommended_package_decoded[key] = label_mappings[key][value]  
    else:
        recommended_package_decoded[key] = value  

if 'State' in recommended_package and isinstance(recommended_package['State'], (int, np.integer)):
    recommended_package_decoded['State'] = state_mapping[recommended_package['State']]
elif 'State' in recommended_package:
    recommended_package_decoded['State'] = recommended_package['State']
else:
    recommended_package_decoded['State'] = state_mapping[predicted_state_index]

# Display the recommendation
st.subheader("🎉 Recommended Travel Package")
st.markdown(f"""
📍 **Destination:** `{recommended_package_decoded['State']}`  
💰 **Budget:** ₹ `{recommended_package_decoded['Budget (INR)']}`  
⏳ **Best Season:** `{recommended_package_decoded['Season']}`  
🎭 **Cultural Highlights:** `{recommended_package_decoded['Cultural Highlights']}`  
🍽 **Food Cost per day:** ₹ `{recommended_package_decoded['Food Cost (INR)']}`  
🏨 **Hotel Cost per night:** ₹ `{recommended_package_decoded['Hotel Cost (INR)']}`  
⭐ **Average Review Rating:** `{recommended_package_decoded['Reviews']} / 5.0`
""")

# Display the dataset for reference
st.subheader("📊 Travel Package Data")
st.dataframe(df[['State', 'Budget (INR)', 'Season', 'Cultural Highlights', 'Food Cost (INR)', 'Hotel Cost (INR)', 'Reviews']].head(10))


# Connect to the database
conn = sqlite3.connect("Dataset and Database/travel_progress.db")
cursor = conn.cursor()

# Fetch the latest recommended package
cursor.execute("SELECT * FROM travel_progress ORDER BY id DESC LIMIT 1")
latest_package = cursor.fetchone()

st.subheader("📊 Your Travel Planning Progress")

if latest_package:
    st.write(f"📍 **Destination:** {latest_package[1]}")
    st.write(f"💰 **Budget:** ₹{latest_package[2]}")
    st.write(f"⏳ **Best Season:** {latest_package[3]}")
    st.write(f"🎭 **Cultural Highlights:** {latest_package[4]}")
    st.write(f"🍽 **Food Cost per day:** ₹{latest_package[5]}")
    st.write(f"🏨 **Hotel Cost per night:** ₹{latest_package[6]}")
    st.write(f"⭐ **Average Review Rating:** {latest_package[7]} / 5.0")

    # Track progress
    flights = st.checkbox("✈️ Flights Booked", value=bool(latest_package[8]))
    hotel = st.checkbox("🏨 Hotel Booked", value=bool(latest_package[9]))
    activities = st.checkbox("🎟 Activities Planned", value=bool(latest_package[10]))
    packing = st.checkbox("🎒 Packing Done", value=bool(latest_package[11]))
    trip_done = st.checkbox("✅ Trip Completed", value=bool(latest_package[12]))

    # Function to update progress
    def update_progress(column, value):
        cursor.execute(f"UPDATE travel_progress SET {column} = ? WHERE id = ?", (value, latest_package[0]))
        conn.commit()

    if flights:
        update_progress("flights_booked", 1)
    if hotel:
        update_progress("hotel_booked", 1)
    if activities:
        update_progress("activities_planned", 1)
    if packing:
        update_progress("packing_done", 1)
    if trip_done:
        update_progress("trip_completed", 1)

    # Calculate progress
    completed_steps = sum([flights, hotel, activities, packing, trip_done])
    total_steps = 5
    progress = (completed_steps / total_steps) * 100

    # Show progress bar
    st.progress(progress / 100)
    st.write(f"**Your progress: {progress:.2f}% completed!**")
    
else:
    st.warning("No travel package found. Please get a recommendation first.")

# Close database connection
conn.close()

