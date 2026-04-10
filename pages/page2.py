from groq import Groq
import streamlit as st
user_input=st.text_input("enter text")
button=st.button("send")
# Initialize the Groq client with your API key
client = Groq(api_key="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")

if button==True:
   # It is recommended to use environment variables for security
   chat_completion = client.chat.completions.create(
      messages=[
   {
      "role":'system',
      "content":'''you are a car lover have abig knowelge about cars,
         ifuser asks you about anything exept cars->replywith i donot know'''
   },
         {
               "role": "user",
               "content": user_input,
         }
      ],
      model="llama-3.3-70b-versatile", # Specify your desired model
   )

   st.write(chat_completion.choices[0].message.content)



