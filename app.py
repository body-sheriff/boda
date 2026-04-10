import streamlit as st
from google import genai





user_input=st.text_input("enter text")
boda=st.button("send")

client = genai.Client( api_key = 'AIzaSyD1b39JDkToj1FXB4ATgVsyVFVmuFcWDh8' )

if boda==True:
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents= user_input ,
)
    st.write(response.text)