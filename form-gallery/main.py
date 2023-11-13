import streamlit as st
import datetime

SAMPLE_DATA_JSON = '''
{
  "type" : "members",
  "members" : [
    {
      "name" : "Alice",
      "age" : 16
    },
    {
      "name" : "Bob",
      "age" : 24
    }
  ]
}
'''

# Button
st.header('Button')
sign_up = st.button('Sign up')
if sign_up:
    st.write('Sign up button pressed')

# Download Button
st.header('Download Button')
download = st.download_button(
    'Download Sample File',
    SAMPLE_DATA_JSON,           # Content of the download file
    file_name='sample.json',    # Name of the download file
)
if download:
    st.write('You download the sample file')


# Text box
st.header('Text Box')
name = st.text_input('Name', key='name')
st.write(f'You entered {st.session_state.name}')
st.write(f'You entered {name}')

# Number box
st.header('Number Box')
age = st.number_input('Age')
st.write(f'Your age is {age}')

# Date box
st.header('Date Box')
birthday = st.date_input(
    'Birthday',
    value=datetime.date(2023, 4, 15),
    format='MM-DD-YYYY',    # Date format
)
st.write(f'Your birthday is {birthday}')

# Time box
st.header('Time Box')
alarm = st.time_input(
    'Alarm',
    value=datetime.time(15, 30, 00),
    step=30*60,    # Stepping interval in seconds. 30 minutes here
)
st.write(f'Alarm set for {alarm}')


# Text Area
st.header('Text Area')
description = st.text_area('Description', key='description')
st.write(f'You entered {st.session_state.description}')
st.write(f'You entered {description}')

# Radio box
st.header('Radio box')
country = st.radio(
    'South East Asia',
    (
        'Brunei', 'Cambodia', 'Indonesia', 'Laos', 'Malaysia', 'Philippines', 'Singapore', 'Thailand', 'Vietnam',
    ),
    3,  # Selected index
)
st.write(f'You selected {country}')

# Checkbox
st.header('Checkbox')
consent = st.checkbox('Agree')
if consent:
    st.write('I agree')

# Toggle
st.header('Toggle')
activate = st.toggle('Activate')
if activate:
    st.write('Activated')

# Select (dropdown) box
st.header('Select (dropdown) box')
transport = st.selectbox(
    'Travel Options',
    (
        'Car',
        'Bus',
        'Rail',
        'Plane',
    ),
    2,  # Selected index
)
st.write(f'You selected {transport}')

# Multiselect (dropdown) box
st.header('Multi-select (dropdown) box')
tags = st.multiselect(
    'Blog tags',
    (
        'Cooking',
        'Recipes',
        'Gardening',
        'Running',
        'Weightlifting',
        'Surfing',
        'Swimming',
        'Reading',
        'Book Review',
    ),
)
st.write(f'Blogs tags are {tags}')

# Slider
st.header('Slider')
percent = st.slider(
    'Select percentage',
    0.0,    # Min value
    100.0,  # Max value
    50.0,   # Selected value
)
st.write(f'Percentage at {percent}')

# Color Picker
st.header('Color Picker')
bg_color = st.color_picker(
    'Background Color',
    '#3366CC',
)
st.write(f'Background color is {bg_color}')
