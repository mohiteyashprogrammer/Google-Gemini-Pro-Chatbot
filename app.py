import streamlit as st
import os
import google.generativeai as genai
import dotenv

from utils import set_background,role_to_streamlit

# Load the environment variables from the .env file
dotenv.load_dotenv()

# Access the environment variables just like you would with os.environ
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_PRO_API"))

 # Setting up a google gemini-pro instance
GOOGLE_GEMINI_PRO = "gemini-pro"
model = genai.GenerativeModel(GOOGLE_GEMINI_PRO)

#set_background("C:\Users\yash mohite\OneDrive\Desktop\Google-Gemini-Pro-Chatbot\Google-Gemini-AI-model.jpg")

# Initialize the chat session by calling the 'start_chat' method of the model.
# The 'history' parameter is passed as an empty list to indicate that there is no previous conversation history.
# Depending on the implementation of the model, this could involve initializing some variables or loading a pre-trained model.
# The returned value would typically be an object representing the chat session.
if "chat" not in st.session_state:# Check if the key "Chat" is not already present in the session_state dictionary.
    st.session_state.chat = model.start_chat(history=[])# This allows the chat session to persist across interactions within the Streamlit app.

# Display the Title
st.title("Welcome To Google Gemini-pro Chatbot")

try:
    # Loop through the chat history and display messages with appropriate roles
    for message in st.session_state.chat.history:
    # Use "role_to_streamlit" function to determine message role (user or assistant)
        role = role_to_streamlit(message.role)
    # Create a chat message with the determined role
        with st.chat_message(role):
            # Display the text content of the message
            st.markdown(message.parts[0].text)

# Handle potential exceptions during message display
except Exception as e:
    # Display an error message to the user
    st.error(e)

# Prompt the user for input
prompt = st.chat_input("I Possess a Will Of Knowledge. What would you like to Know?, Enter a Promot here")

# Check if the user actually entered something
if prompt:
    # Display the user's prompt as a chat message
    st.chat_message("user").markdown(prompt)
    # Send the user's prompt to the chat model and get a response
    response = st.session_state.chat.send_message(prompt)
    # Display the assistant's response as a chat message
    with st.chat_message("assistant"):
        st.markdown(response.text)


 

