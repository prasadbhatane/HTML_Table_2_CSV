import pandas as pd
import numpy as np
import streamlit as st
import requests
from download_script import download


@st.cache(persist=True)
def get_data(my_url):
    req = requests.get(my_url)
    data =  pd.read_html(req.text)
    return data


st.title("HTML Table to CSV Converter")
st.sidebar.title("HTML Table to CSV Converter")
st.sidebar.markdown('### Please paste your URL here :')

my_url = st.sidebar.text_input(label ="", value='https://www.codechef.com/problems/school/?itm_medium=navmenu&itm_campaign=problems', key='my_url')
if my_url:
    if 'https://' in my_url:
        data = get_data(my_url)
        if len(data) == 0:
            st.write("No Table Found")
        else:
            tbls = [i for i in range(1, len(data)+1)]
            st.markdown('### Select Table :')
            
            slct = st.selectbox(label="",options=tbls)
            selected_tbl = data[slct-1]
            st.dataframe(selected_tbl)
    else:
        st.write("INVALID URL !!!")


    download(selected_tbl)





