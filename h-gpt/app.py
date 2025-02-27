# importing genai a library which will allow us to use gemini model
from google import  genai
import streamlit as st
import os # is is imported to use environment variables

st.title("Welcome to H-Gpt")
st.header("Lil bro of ChatGpt ;)")
api_key = os.environ.get("GOOGLE_API_KEY")

# function that will call the api
def get_gemini_response(user_input,api_key):
    if api_key is None:
        return "APi key issue"

    else:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
        model = "gemini-2.0-flash", contents=user_input)
        return response.text


#taing input from the user
user_input = st.chat_input("Ask H-Gpt anything")

# a plaveholder value that will later be the output/respone of llm
response_placeholder = st.empty()

if user_input:
    # with will automatically stops the spinner when function will be executed
    with st.spinner("Generating response..."):
        response_text = get_gemini_response(user_input,api_key)
        response_placeholder.write(response_text)


# print(response.text)