import streamlit as st
import pandas as pd
import numpy as np
from st_pages import Page, Section, show_pages, add_page_title

#side bar part refer https://github.com/blackary/st_pages
# add_page_title()

st.title('''Welcome Group 4's World!''')


# Display the image, which should be centered with the CSS above
st.image('asset/intro.png', width=500)
show_pages(
    [
        Page("streamlit.py", "Main Introduce", "💡"),
        Page("other_pages/writting.py", "Writting a Article!", "📝"),
        Page("other_pages/trend_predict.py", "Predict Article's View!!", "🔥"),
        # Unless you explicitly say in_section=False
    ]
)