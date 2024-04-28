import streamlit as st
import datetime
import pandas as pd
import numpy as np
from st_pages import Page, Section, show_pages, add_page_title
import requests

def send_data(title, txt, tag, deadline):
    url = "https://d29e-104-199-156-150.ngrok-free.app" # gn api link
    path = '/api/predict'  # Replace with your API endpoint
    endpoint = url + path
    tags = [t.strip() for t in tag.split(',')]
    deadline_datetime = datetime.datetime.combine(deadline, datetime.time.min)
    time_diff_seconds = (deadline_datetime - datetime.datetime.now()).total_seconds()
    data = {
        "content": txt,
        "title": title,
        "tags": tags,  # Assuming tags are comma-separated
        "deadline" : int(time_diff_seconds) 
    }
    response = requests.post(endpoint, json=data)
    return response.status_code, response.json() 


st.title('Writting a Article!')

with st.form(key='my_form'):
    title = st.text_input(label='Tite', placeholder='Insert Article Title')
    txt = st.text_area(
        label='Contents',
        placeholder='Insert the Contents!',
        height=500,
    )
    tag = st.text_input(label='Tags', placeholder='Insert Article Tags likes apple, beer')
    deadline = st.date_input("When's artucle deadline", datetime.date(2024, 5, 5))
    submit_button = st.form_submit_button(label='Verify')

    if submit_button:
        
        with st.spinner('Wait for it...'):
            status_code, response = send_data(title, txt, tag, deadline)
        if status_code == 200:
            st.success(f'Data successfully Analysis Predict View is {response}')
        else:
            st.error(f'Failed to submit data: {response}')