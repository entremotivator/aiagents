# app.py
import streamlit as st
from utils.tool_data import get_all_tools
from utils.recommendations import recommend_tools

st.set_page_config(page_title="AI Tools Directory", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Select a page:", 
    ["Home", "Large Language Models", "Vector Databases", "AI Embedders", 
     "Local Tools", "UI Tools", "Cloud-Based Tools", "Tool Comparison", "Recommendations"]
)

# Additional sidebar options
st.sidebar.markdown("---")
st.sidebar.title("Search & Filter Tools")
search_query = st.sidebar.text_input("Search for tools:")
category_filter = st.sidebar.multiselect("Filter by Category", ["LLM", "Vector DB", "Embedder", "Cloud", "Local", "UI"])

# Theme selection
st.sidebar.title("Theme")
theme = st.sidebar.radio("Choose Theme", ["Light", "Dark", "Default"])

# Load the corresponding page
if page == "Home":
    from pages.index import display_home
    display_home(search_query, category_filter)
elif page == "Large Language Models":
    from pages.large_language_models import display_large_language_models
    display_large_language_models()
elif page == "Vector Databases":
    from pages.vector_databases import display_vector_databases
    display_vector_databases()
elif page == "AI Embedders":
    from pages.ai_embedders import display_ai_embedders
    display_ai_embedders()
elif page == "Local Tools":
    from pages.local_tools import display_local_tools
    display_local_tools()
elif page == "UI Tools":
    from pages.ui_tools import display_ui_tools
    display_ui_tools()
elif page == "Cloud-Based Tools":
    from pages.cloud_based_tools import display_cloud_based_tools
    display_cloud_based_tools()
elif page == "Tool Comparison":
    from pages.tool_comparison import display_comparison
    display_comparison()
elif page == "Recommendations":
    recommend_tools()
