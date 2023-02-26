import os
import streamlit as st
import openai


def open_file(filepath):
    if 'openai' in st.secrets:
        return st.secrets['openai']['api_key']
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def gpt3_completion(prompt, engine='text-davinci-002', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['VMware Support:', 'USER:']):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
    text = response['choices'][0]['text'].strip()
    return text


def main():
    st.title('OpenAI Chatbot')
    conversation = st.text_area('Conversation', height=400)
    user_input = st.text_input('User Input')
    if st.button('Send'):
        conversation += 'USER: ' + user_input + '\n'
        prompt = open_file('prompt_chat.txt').replace('<<BLOCK>>', conversation)
        prompt += 'VMware Support:'
        response = gpt3_completion(prompt)
        conversation += 'VMware Support: ' + response + '\n'
    st.write(conversation)


if __name__ == '__main__':
    main()