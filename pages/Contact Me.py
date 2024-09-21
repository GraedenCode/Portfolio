import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key='email_form'):
    user_email = st.text_input('Your E-mail Address', value='')
    raw_message = st.text_area('Your Message',value='')
    message = f"""\
Subject: Portfolio Message

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button('Submit')
    if button:
        send_email(user_email, message)
        st.info("Message Sent!")