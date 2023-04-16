import streamlit as st
from pages import heart_disease_visualization, predict_cost_machine_learning, data_uploader
from style import set_background
set_background()

# Create a dropdown menu with the page options
menu = st.selectbox('Select a page', ['Main Page', 'Heart Disease Visualization', 'Predict Cost Machine Learning', 'Data Uploader'])

# Show the selected page based on the dropdown menu option
if menu == 'Main Page':
    set_background()
    st.title('Main Page')
    st.subheader('Welcome to the main page!')
    st.write('These web app contains some of streamlit projects')
    st.write('Please select menu above to visit those pages!')
    st.write('Thank you 😄')
    if st.checkbox('Created by'):
        st.success('Firdaus Wahyu Nugroho')

elif menu == 'Heart Disease Visualization':
    set_background()
    heart_disease_visualization.show()
elif menu == 'Predict Cost Machine Learning':
    set_background()
    predict_cost_machine_learning.show()
elif menu == 'Data Uploader':
    set_background()
    data_uploader.show()
