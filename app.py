import streamlit as st
import json
from model_helper import load



        
st.sidebar.image("img.png",use_column_width=True)
st.sidebar.title("SMS Classification")

st.header("spam text message calssification".upper())
st.empty()

with st.spinner("loading trained model file"):
    model = load()
    input = []

option2 = st.sidebar.checkbox("creator info")
if option2:
    st.info("# Kaushal Mishra")
    st.info("BBDU, BCA")

option3 = st.sidebar.checkbox("inspire me")
if option3:
    st.sidebar.success("stay safe stay home")

option4 = st.sidebar.checkbox("Project Info")
if option4:
    st.header("Project details")
    st.success('''
        SMS  spam filtering challenge is similar to email spam filtering, with the difference that they can send  a limited number  of characters only.  It is noticed that almost all spam SMS text may contain a very close pattern  due  to  this  limitation.
It  incorporates  some  “catch information, usually a call back number, reply SMS number or a URL (Uniform Resource Locator) that they can visit, at the least, a keyword that they can search words” to  attract
    ''')

option5 = st.sidebar.checkbox("dataset link")
if option5:
    st.sidebar.success("https://www.kaggle.com/team-ai/spam-text-message-classification/data")

option6 = st.sidebar.checkbox("dataset distribution")
if option6:
    st.sidebar.image('dataset_dist.png',use_column_width=True)

option7 = st.sidebar.checkbox("Sms spam/ham frequency")
if option7:
    st.sidebar.image('spam_ham_dist.png',use_column_width=True)

data = st.text_area("copy a sms message here")
if data:
    with st.spinner('please wait, while we analyse this message'):
        input.append(data)
        prediction = model.predict(input)[0]
        if prediction == "ham":
            st.success(f"## Message is classified as Safe (not spam)")
            st.image('ham.jpg',width=100)
        else:
            st.warning(f"## Message is classified as {prediction}")
            st.image('spam.jpg',width=100)
else:
    st.error("enter some message to analyse")

if data and st.checkbox("other info"):
    st.write(f"length of message {len(data)}")
    st.write(f"length of words {len(data.split())}")
    st.write(data.split())

