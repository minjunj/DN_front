import streamlit as st

# Title of the app
st.title("Predict Article's View!!")

custom_css = """
<style>
.color-container {
    background-color: #212121; /* Background color of the container */
    border-radius: 5px; /* Rounded corners */
    padding: 10px; /* Space inside the container */
    margin-bottom: 20px; /* Space between containers */
    border: 2px solid #424242; /* White contour line */
}
.color-text {
    color: white;
    font-weight: bold;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Main container
with st.container():

    for i in range(10): 
        st.markdown(f'<div class="color-container"><p class="color-text">Box {i+1}: Custom styled container</p></div>', unsafe_allow_html=True)
