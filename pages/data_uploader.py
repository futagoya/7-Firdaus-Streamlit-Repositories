import streamlit as st
import pandas as pd
import seaborn as sns
from style import set_background
set_background()

st.sidebar.success('Select a page above')

def show():
    st.title('Data Uploader')
    st.write('This is the Data Uploader page.')

    #1. Create the Title
    st.title('Data Analysis Visualization on Streamlit')
    st.subheader('This analysis is using python and streamlit')
    
    #2. Upload the Dataset
    upload = st.file_uploader('Please upload your dataset(in CSV format)')
    if upload is not None:
        data=pd.read_csv(upload)
        
    #3. Showing the Dataset
    if upload is not None:
        if st.checkbox('Preview Dataset'):
            if st.button("Show the top rows"):
                st.write(data.head())
            if st.button("Show the bottom rows"):
                st.write(data.tail())
    
    #4. Check the Datatypes
    if upload is not None:
        if st.checkbox("Show the Datatypes of each column"):
           st.text("Dtypes")
           st.write(data.dtypes)
           
    #5. Find the Shape of Dataset (Number of Rows & Columns)
    if upload is not None:
        data_shape = st.radio('What information do you want to get?',('Rows',
                                                                      'Columns'))
        if data_shape == 'Rows':
            st.text('Number of Rows')
            st.write(data.shape[0])
        
        if data_shape == 'Columns':
            st.text('Number of Columns')
            st.write(data.shape[1])
    
    #6. Show the Null value
    st.set_option('deprecation.showPyplotGlobalUse', False)
    if upload is not None:
        test=data.isnull().values.any()
        if test == True:
            if st.checkbox('Show Null values in Dataset'):
                sns.heatmap(data.isnull())
                st.pyplot()
        else:
            st.success('Yeay! There is no Null values in Dataset!')
    
    #7. Find duplicate values on dataset
    if upload is not None:
        test=data.duplicated().any()
        if test == True:
            st.warning('This dataset contains duplicated value')
            dup=st.selectbox('Do you want to drop the duplicated value?', \
                             ('Select one','Yes','No'))
            if dup == 'Yes':
                data=data.drop_duplicates()
                st.text('Duplicate value has been dropped')
            if dup == 'No':
                st.text('Okay, no problem')
    
    #8. Show the summary statistics of dataset
    if upload is not None:
        if st.checkbox('Get the summary statistics of dataset'):
            st.write(data.describe(include='all'))
    
    #9. About
    if st.button('About app'):
        st.text('Built in Streamlit')
        st.text('Thanks to them!')
    
    #10. By
    if st.checkbox('Created by:'):
        st.success('Firdaus Wahyu Nugroho')