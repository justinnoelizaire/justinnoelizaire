import streamlit as st
import pandas as pd
import plotly.express as px

#page configuration
st.set_page_config(page_title="Basketball Stats Explorer", page_icon="🏀")

# Title and description
st.title("🏀 Basketball Stats Explorer")
st.markdown("Welcome to the Basketball Stats Explorer! Explore basic basketball statistics and information.")

#sample player data
player_data = {
    'Player': ['LeBron James', 'Stephen Curry', 'Kevin Durant', 'Giannis Antetokounmpo', 'Luka Doncic'],
    'Points_Per_Game': [25.0, 28.5, 29.1, 30.2, 32.5],
    'Assists_Per_Game': [7.8, 6.3, 5.5, 6.1, 8.0],
    'Rebounds_Per_Game': [7.3, 4.5, 6.9, 11.2, 8.7],
    'Team': ['Lakers', 'Warriors', 'Suns', 'Bucks', 'Mavericks']
}

df = pd.DataFrame(player_data)

# Sidebar
st.sidebar.header("Player Statistics")
selected_stat = st.sidebar.selectbox(
    "Choose a statistic to visualize:",
    ['Points_Per_Game', 'Assists_Per_Game', 'Rebounds_Per_Game']
)

# Main content
st.subheader(f"Player {selected_stat.replace('_', ' ')}")

#bar chart
fig = px.bar(
    df,
    x='Player',
    y=selected_stat,
    color='Team',
    title=f'{selected_stat.replace("_", " ")} by Player'
)
st.plotly_chart(fig)

#player data table
st.subheader("Player Data Table")
st.dataframe(df)

#Interactive player selector
st.subheader("Player Comparison")
selected_player = st.selectbox("Select a player to view their stats:", df['Player'].tolist())

if selected_player:
    player_stats = df[df['Player'] == selected_player].iloc[0]
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Points", f"{player_stats['Points_Per_Game']:.1f}")
    with col2:
        st.metric("Assists", f"{player_stats['Assists_Per_Game']:.1f}")
    with col3:
        st.metric("Rebounds", f"{player_stats['Rebounds_Per_Game']:.1f}")

# Fun fact section
st.sidebar.markdown("---")
st.sidebar.subheader("Did you know? 🤔")
basketball_facts = [
    "The NBA three-point line is 23.75 feet from the basket.",
    "A basketball game typically lasts 48 minutes in the NBA.",
    "The basketball was first orange in color in the late 1950s.",
    "Kareem Abdul-Jabbar holds the record for most points in NBA history.",
    "The first basketball game was played with a soccer ball."
]
st.sidebar.write(basketball_facts[0])