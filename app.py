apikey = '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'
import os 

import streamlit as st
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = apikey


st.title('ASK ME')
prompt = st.text_input('Plug in your prompt here') 

llm = OpenAI(temperature=0.9) 
if prompt: 
    response = llm(prompt)
    st.write(response)
