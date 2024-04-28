import streamlit as st
import requests
# Title of the app
st.title("Predict Article's Top Rate View!!")

def send_data():
    url = 'https://d29e-104-199-156-150.ngrok-free.app' # dn be api link 
    path = '/api/rank'  # Replace with your API endpoint
    endpoint = url + path
    response = requests.get(endpoint)
    return response.json() 

custom_css = """
<style>
.color-container {
    background-color: #212121; /* Background color of the container */
    border-radius: 5px; /* Rounded corners */
    padding: 10px; /* Space inside the container */
    margin-bottom: 20px; /* Space between containers */
    border: 2px solid #424242; /* White contour line */
}
.color-text a {
    color: white; /* Hyperlink color set to white, same as the regular text */
    font-weight: bold;
    text-decoration: none; /* Removes underline from hyperlinks */
}
.color-text a:hover {
    text-decoration: none; /* No change on hover, can be set to underline if desired */
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
send_data()
# Main container
with st.container():
    with st.spinner('Wait for it...'):
        trend_list = send_data()
    for i in trend_list:
        api = f"https://api.ziggle.gistory.me/notice/{i[0]}" # ziggle be api 
        try:
            response = requests.get(api)
            r = response.json()["contents"][0]["title"]
            hyperlink = f"https://ziggle.gistory.me/ko/notice/{i[0]}" # ziggle fe link
            st.markdown(f'<div class="color-container"><p class="color-text"><a href="{hyperlink}" target="_blank">{response.json()["contents"][0]["title"]}       Predict : {i[1]}</a></p></div>', unsafe_allow_html=True)
        except:
            pass
