import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Groceries Data Visualization')

DATA_URL = 'https://github.com/BeinmaBeima/ClassDemo/blob/main/Groceries_dataset.csv'

@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('10 Most Frequently Purchased Items')
item_counts = data['itemDescription'].value_counts().head(10)
st.bar_chart(item_counts)
