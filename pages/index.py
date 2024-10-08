# pages/index.py
import streamlit as st
from utils.tool_data import get_tools_by_query

def display_home(search_query=None, category_filter=None):
    st.title("Welcome to the AI Tools and Technologies Directory")
    st.write("Use the search and filter options in the sidebar to find specific tools.")

    if search_query:
        results = get_tools_by_query(search_query, category_filter)
        st.subheader(f"Search Results for: '{search_query}'")
        if not results:
            st.write("No tools found.")
        else:
            for tool in results:
                st.write(f"### {tool['name']}")
                st.write(f"**Category:** {tool['category']}")
                st.write(tool['description'])
                st.markdown(f"[More Info]({tool['link']})")
    else:
        st.write("Navigate to different categories using the sidebar to explore AI tools.")
