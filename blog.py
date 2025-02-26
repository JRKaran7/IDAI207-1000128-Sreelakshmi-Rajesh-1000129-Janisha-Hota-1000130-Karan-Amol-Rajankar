import streamlit as st
import json
import os
from datetime import datetime

# File to store blog data
BLOG_FILE = "blog_data.json"

# Ensure the JSON file exists
if not os.path.exists(BLOG_FILE):
    with open(BLOG_FILE, "w") as f:
        json.dump([], f)

# Load blog posts
def load_posts():
    with open(BLOG_FILE, "r") as f:
        return json.load(f)

# Save new blog post
def save_post(title, content):
    posts = load_posts()
    new_post = {
        "title": title,
        "content": content,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    posts.insert(0, new_post)  # Add new post at the top
    with open(BLOG_FILE, "w") as f:
        json.dump(posts, f, indent=4)

# Streamlit UI
st.set_page_config(page_title="📖 My Blog", layout="wide")
st.title("📖 My Personal Blog")

# Sidebar for adding a new post
st.sidebar.header("📝 Add a New Blog Post")
title = st.sidebar.text_input("Title")
content = st.sidebar.text_area("Content (supports Markdown)")
if st.sidebar.button("Post"):
    if title and content:
        save_post(title, content)
        st.sidebar.success("Post added successfully!")
        st.rerun()
    else:
        st.sidebar.error("Title and Content are required!")

# Search Functionality
search_query = st.text_input("🔍 Search Posts", "")
posts = load_posts()

if search_query:
    posts = [post for post in posts if search_query.lower() in post["title"].lower()]

# Display blog posts
for post in posts:
    st.markdown(f"## {post['title']}")
    st.markdown(f"🗓️ *{post['date']}*")
    st.markdown(post["content"])
    st.markdown("---")

# Custom CSS for styling
st.markdown("""
    <style>
        body { background-color: #f7f7f7; }
        .block-container { max-width: 750px; }
        h1 { color: #4CAF50; }
        h2 { color: #333; }
    </style>
    """, unsafe_allow_html=True)
