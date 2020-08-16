import streamlit as st
import base64

def download(selected_tbl):
	csv_file = selected_tbl.to_csv(index=False)
	encoded = base64.b64encode(csv_file.encode()).decode()
	st.sidebar.markdown('### Click Here To Download the CSV File 👇')
	href = f'<a href="data:file/csv;base64,{encoded}" download="html2csv.csv">DOWNLOAD</a>'
	st.sidebar.markdown(href, unsafe_allow_html=True)