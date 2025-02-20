import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from datetime import datetime

# Page configuration
st.set_page_config(page_title="Mind Check", page_icon="🧠", layout="centered")

# Title
st.title("Mental Health Check-In App")
st.write("Track your mood, journal your thoughts, and stay motivated!")

# Initialize session state for mood and journal data
if 'mood_data' not in st.session_state:
    st.session_state.mood_data = pd.DataFrame(columns=["Date", "Mood"])

if 'journal_data' not in st.session_state:
    st.session_state.journal_data = pd.DataFrame(columns=["Date", "Entry"])

# Function to fetch a motivational quote
def get_quote():
    try:
        response = requests.get("https://api.quotable.io/random")
        if response.status_code == 200:
            quote = response.json()["content"]
            author = response.json()["author"]
            return f'"{quote}" - {author}'
    except:
        return "Stay positive and keep growing!"

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Mood Tracker", "Journal", "Progress"])

# Home Page
if page == "Home":
    st.header("Welcome to Your Mental Health Check-In App!")
    st.write("Use this app to track your mood, journal your thoughts, and access motivational resources.")
    st.write("### Daily Motivational Quote")
    st.write(get_quote())

# Mood Tracker Page
elif page == "Mood Tracker":
    st.header("Mood Tracker")
    st.write("How are you feeling today?")
    
    # Mood input
    mood = st.select_slider("", options=["😔 Sad", "😐 Neutral", "😊 Happy"], value="😐 Neutral")
    
    if st.button("Log Mood"):
        # Create a new entry
        new_entry = pd.DataFrame({"Date": [datetime.now()], "Mood": [mood]})
        
        # Append the new entry to the DataFrame using pd.concat()
        st.session_state.mood_data = pd.concat([st.session_state.mood_data, new_entry], ignore_index=True)
        st.success("Mood logged successfully!")
    
    # Display mood history
    st.write("### Your Mood History")
    if not st.session_state.mood_data.empty:
        st.session_state.mood_data['Date'] = pd.to_datetime(st.session_state.mood_data['Date'])
        st.session_state.mood_data = st.session_state.mood_data.sort_values(by="Date")
        fig = px.line(st.session_state.mood_data, x="Date", y="Mood", title="Mood Over Time")
        st.plotly_chart(fig)
    else:
        st.write("No mood data available yet.")

# Journal Page
elif page == "Journal":
    st.header("Journal")
    st.write("Write about your day, thoughts, or feelings.")
    
    # Journal input
    journal_entry = st.text_area("Write your journal entry here:")
    
    # Save journal entry
    if st.button("Save Journal Entry"):
        if journal_entry.strip():
            # Create a new entry
            new_entry = pd.DataFrame({"Date": [datetime.now()], "Entry": [journal_entry]})
            
            # Append the new entry to the DataFrame using pd.concat()
            st.session_state.journal_data = pd.concat([st.session_state.journal_data, new_entry], ignore_index=True)
            st.success("Journal entry saved!")
        else:
            st.warning("Please write something before saving.")
    
    # Display journal history
    st.write("### Your Journal Entries")
    if not st.session_state.journal_data.empty:
        st.session_state.journal_data['Date'] = pd.to_datetime(st.session_state.journal_data['Date'])
        st.session_state.journal_data = st.session_state.journal_data.sort_values(by="Date", ascending=False)
        st.write(st.session_state.journal_data)
    else:
        st.write("No journal entries yet.")

# Progress Page
elif page == "Progress":
    st.header("Your Progress")
    st.write("Here's an overview of your mental health journey.")
    
    # Mood progress
    st.write("### Mood Progress")
    if not st.session_state.mood_data.empty:
        mood_counts = st.session_state.mood_data['Mood'].value_counts().reset_index()
        mood_counts.columns = ['Mood', 'Count']
        fig = px.bar(mood_counts, x='Mood', y='Count', title="Mood Distribution")
        st.plotly_chart(fig)
    else:
        st.write("No mood data available yet.")
    
    # Journal progress
    st.write("### Journal Progress")
    if not st.session_state.journal_data.empty:
        st.write(f"Total Journal Entries: {len(st.session_state.journal_data)}")
        st.write("### Latest Journal Entry")
        st.write(st.session_state.journal_data.iloc[0]['Entry'])
    else:
        st.write("No journal entries yet.")

# Footer
st.sidebar.write("---")