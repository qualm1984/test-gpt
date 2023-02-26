import os
import streamlit as st
import openai


#def get_api_key():
 #   return os.environ.get('OPENAI_API_KEY')

def get_api_key():
    api_key = os.environ.get('OPENAI_API_KEY')
    print('API key:', api_key)
    return api_key

print(get_api_key)
