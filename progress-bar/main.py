import streamlit as st
import time

# Set the title.
st.write('Loading data...')

# Add a placeholder for the progres title and progress bar
progress_text = st.empty()   # Progress title
bar = st.progress(0)            # Progress bar

for i in range(100):
    progress_text.text(f'{i+1}%')
    bar.progress(i+1)
    time.sleep(0.2)

st.write('Done...')
