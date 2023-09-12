import streamlit as st

# Initialize session state variables
if "openai_api_key" not in st.session_state:
    st.session_state.openai_api_key = ""

if "serper_api_key" not in st.session_state:
    st.session_state.serper_api_key = ""

st.set_page_config(page_title="Home", page_icon="🦜️🔗")

st.header("Welcome to LLM Heaven! 👋")

st.markdown(
    """
	This page is inspired by the multiple LangChain demos available at: https://github.com/alphasecio/langchain-examples
	However, this uses an LLM model and togheter with LangChain exploits its capabilities, I have another demo that fine tunes an NLP model on the CoLA dataset [here](https://alejohz.github.io/).
    Step into the world of language and AI synergy! Explore a captivating showcase of cutting-edge text technologies.
	
	Unleash the power of linguistic models and uncover the magic of automated language understanding.
	Experience innovation at your fingertips.
	
	##### Web Search
    * A sample app for web search queries using LangChain and Serper API.

    ##### Settings
    * Set your API keys for the apps.

    """  # noqa: E501
)
