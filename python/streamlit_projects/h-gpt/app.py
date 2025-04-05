# importing genai a library which will allow us to use gemini model
import google.generativeai as genai # type: ignore
import streamlit as st
import os # is is imported to use environment variables

st.title("Welcome to H-Gpt")
st.header("Lil bro of ChatGpt ;)")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function that will call the api
def get_gemini_response(user_input):    
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(user_input, stream=True)
    return response


#taing input from the user
user_input = st.chat_input("Ask H-Gpt anything")

# a plaveholder value that will later be the output/respone of llm
response_placeholder = st.empty()

if user_input:
    # with will automatically stops the spinner when function will be executed
    with st.spinner("Generating response..."):
        response_text = get_gemini_response(user_input)
        full_response = ""
        for chunk in response_text:
            if chunk.text:
                full_response += chunk.text
                response_placeholder.write(full_response)


# print(response.text)
