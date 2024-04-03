import streamlit as st
import string
import pickle
import requests
import numpy as np

st.title("Phishing website classifier")
url = st.text_input("Paste the url here")


def count_redirections(url):
    redirection_count = 0
    current_url = url

    try:
        while True:
            response = requests.head(current_url, allow_redirects=True)
            if response.history:
                redirection_count += 1
                current_url = response.url
            else:
                break
    except Exception as e:
        st.error(f"Error: {e}")
        return None

    return redirection_count


model_input = []

if st.button('Predict') and url != '':
    model_input.append(len(url))
    model_input.append(url.count('.'))
    model_input.append(url.count('-'))
    model_input.append(url.count('_'))
    model_input.append(url.count('/'))
    model_input.append(url.count('?'))
    model_input.append(url.count('='))
    model_input.append(url.count('@'))
    model_input.append(url.count('&'))
    model_input.append(url.count('!'))
    model_input.append(url.count(' '))
    model_input.append(url.count('~'))
    model_input.append(url.count(','))
    model_input.append(url.count('+'))
    model_input.append(url.count('*'))
    model_input.append(url.count('#'))
    model_input.append(url.count('$'))
    model_input.append(url.count('%'))

    redirection_count = count_redirections(url)

    if redirection_count is None:
        st.error("Error occurred during URL processing.")
    else:
        model_input.append(redirection_count)

        model_input = np.array(model_input).reshape(1, -1)
        print(model_input)

        result = 0
        model = pickle.load(open('model.pkl', 'rb'))
        result = model.predict(model_input)[0]
        print(result)
        if result == 0:
            st.error("Phishing website")
        else:
            st.success("Legit website")
