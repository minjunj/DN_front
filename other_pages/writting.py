import streamlit as st
import datetime
import pandas as pd
import numpy as np
from st_pages import Page, Section, show_pages, add_page_title
import requests

def send_data(title, txt, tag, deadline):
    url = "https://da39-34-125-154-224.ngrok-free.app/api/predict"  # Replace with your API endpoint
    tags = [t.strip() for t in tag.split(',')]
    deadline_datetime = datetime.datetime.combine(deadline, datetime.time.min)
    time_diff_seconds = (deadline_datetime - datetime.datetime.now()).total_seconds()
    data = {
        "content": txt,
        "title": title,
        "tags": tags,  # Assuming tags are comma-separated
        "deadline" : int(time_diff_seconds) 
    }
    print(data)
    response = requests.post(url, json=data)
    return response.status_code, response.json() 


st.title('Writting a Article!')

with st.form(key='my_form'):
    title = st.text_input(label='Tite', placeholder='Insert Article Title')
    txt = st.text_area(
        label='Contents',
        placeholder='Insert the Contents!',
        height=500,
    )
    tag = st.text_input(label='Tags', placeholder='Insert Article Tags likes #apple, #beer')
    deadline = st.date_input("When's artucle deadline", datetime.date(2024, 5, 5))
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        status_code, response = send_data(title, txt, tag, deadline)
        if status_code == 200:
            st.success('Data successfully submitted!')
        else:
            st.error(f'Failed to submit data: {response}')