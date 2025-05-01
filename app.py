import streamlit as st
import requests
import json
from PIL import Image

#load icon
st.set_page_config(
    page_title = " Joi - Mental Health Assistant",
    page_icon = "JOI.ico",
    layout = "wide"
)
# dEcoration
st.title("Joi")
st.write("You look so lonely. I can fix that")
st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('C:\\Users\\ASUS\\Desktop\\weirds_work\\JoiAkka.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
            margin: 0;
        }}
        .stAppViewContainer {{
            background-image: url('C:\\Users\\ASUS\\Desktop\\weirds_work\\JoiAkka.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
            margin: 0;
        }}
        </style>
        """,
        unsafe_allow_html=True
)

# Store conversation history in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Rasa server URL (make sure your Rasa server is running)
rasa_url = "http://localhost:5005/webhooks/rest/webhook"

# Function to communicate with Rasa bot
def get_bot_response(user_message):
    headers = {"Content-Type": "application/json"}
    data = {"sender": "user", "message": user_message}
    response = requests.post(rasa_url, headers=headers, data=json.dumps(data))
    return response.json()

# Input box for user message
user_input = st.text_input("You: ", key="input")

if st.button("Send"):
    # Append user message to session state
    st.session_state["messages"].append(f"You: {user_input}")

    # Get bot response
    bot_responses = get_bot_response(user_input)

    # Display bot responses
    for bot_response in bot_responses:

        # To DEbug
        #st.write(bot_response)  # Print the entire response to debug


        if 'text' in bot_response:
            st.session_state["messages"].append(f"🧚🏻‍♀️: {bot_response['text']}")
        else:
            st.session_state["messages"].append(f"Bot response is missing the 'text' key: {bot_response}")

#        st.session_state["messages"].append(f"Bot: {bot_response['text']}")

# Display conversation history
for message in st.session_state["messages"]:
    st.write(message)
