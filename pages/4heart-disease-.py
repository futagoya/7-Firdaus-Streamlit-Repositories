#Data Analysis using Python and Streamlit
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.sidebar.success('Select a page above')

#0. Import Data 
url = 'https://raw.githubusercontent.com/futagoya/5-data-analysis-heart-disease/main/heart.csv'
data = pd.read_csv(url)

#0.1 Title
st.title('Heart Disease Analysis on Streamlit')
st.subheader('This analysis is using python and streamlit')
st.write("Heart Disease Dataset tells datas about people who has \
         Less/More Chance getting Heart Attact with their body's statistics")

st.write("Here is the dataset's preview")
st.write(data.head())

# Options for user to select
analysis_options = ['1. Data Correlation',
                    '2. Heart Disease Distribution by Sex',
                    '3. Heart Disease Distribution by Age & Heart Disease Status',
                    '4. Chest Pain Type by Sex & Heart Disease Status',
                    '5. Fasting Blood Sugar by Sex and Heart Disease Status',
                    '6. Resting Blood Sugar by Sex and Heart Disease Status',
                    '7. Cholesterol Level by Sex and Heart Disease Status']

# Create multiselect widget
selected_options = st.multiselect('Select analysis(es)', analysis_options, default=analysis_options)

#1. Data Correlation
if '1. Data Correlation' in selected_options:
    st.subheader('1. Data Correlation')
    correlation_matrix=data.corr()
    sns.set_style("white")
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', mask=mask, square=True, ax=ax)
    st.pyplot(fig)

#2. Heart Disease Distribution by Sex
if '2. Heart Disease Distribution by Sex' in selected_options:
    st.subheader('2. Heart Disease Distribution by Sex')
    sns.set_style("white")
    custom_palette = sns.color_palette(['#1f77b4', '#2ca02c'])
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x=data['target'], hue=data['sex'], palette=custom_palette, ax=ax)
    # set the labels and legend
    ax.set_xticklabels(['Less chance', 'More chance'], fontsize=12)
    ax.set_xlabel('Heart Disease', fontsize=14)
    ax.set_ylabel('Count', fontsize=14)
    ax.legend(title='Sex', labels=['Female', 'Male'], fontsize=12)
    # add a title to the plot
    ax.set_title('Heart Disease Distribution by Sex', fontsize=16)
    st.pyplot(fig)

#3.Heart Disease Distribution by Age & Heart Disease Status
if '3. Heart Disease Distribution by Age & Heart Disease Status' in selected_options:
    st.subheader('3. Heart Disease Distribution by Age & Heart Disease Status')
    palette = sns.color_palette(['#1f77b4', '#2ca02c'])
    sns.set_style("whitegrid")
    sns.set_palette(palette)
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(16, 6))
    sns.kdeplot(data[data['target']==0][data['sex']==0]['age'], shade=True, ax=ax1, label='Female')
    sns.kdeplot(data[data['target']==0][data['sex']==1]['age'], shade=True, ax=ax1, label='Male')
    sns.kdeplot(data[data['target']==1][data['sex']==0]['age'], shade=True, ax=ax2, label='Female')
    sns.kdeplot(data[data['target']==1][data['sex']==1]['age'], shade=True, ax=ax2, label='Male')
    
    #3.1 Less Chance
    ax1.set_xlabel('Age/Less Chance', fontsize=14)
    ax1.set_ylabel('Density', fontsize=14)
    ax1.set_title('Age Distribution for Target = 0 or Less Chance of Heart Disease', fontsize=16)
    # ax1.legend(title='Sex', labels=['Female', 'Male'], fontsize=12)
    ax1.legend(title='Sex', fontsize=12)
    
    
    #3.2 More Chance
    ax2.set_xlabel('Age/More Chance', fontsize=14)
    ax2.set_ylabel('Density', fontsize=14)
    ax2.set_title('Age Distribution for Target = 1 or More Chance of Heart Disease', fontsize=16)
    # ax2.legend(title='Sex', labels=['Female', 'Male'], fontsize=12)
    ax2.legend(title='Sex', fontsize=12)
    
    
    sns.despine(ax=ax1)
    sns.despine(ax=ax2)
    
    st.pyplot(fig)

#4. Chest Pain Type by Sex & Heart Disease Status
if '4. Chest Pain Type by Sex & Heart Disease Status' in selected_options:
    st.subheader('4. Chest Pain Type by Sex & Heart Disease Status')
    palette = sns.color_palette(['#1f77b4', '#2ca02c'])
    sns.set_style("whitegrid")
    sns.set_palette(palette)
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 6))
    
    sns.countplot(x=data[data['target']==0]['cp'], hue=data[data['target']==0]['sex'], palette=palette, ax=ax1)
    sns.countplot(x=data[data['target']==1]['cp'], hue=data[data['target']==1]['sex'], palette=palette, ax=ax2)
    
    #4.1 Less Chance
    ax1.set_xlabel('Chest Pain Type', fontsize=14)
    ax1.set_ylabel('Count', fontsize=14)
    ax1.set_title('Less Chance', fontsize=16)
    ax1.legend(title='Sex', labels=['Female', 'Male'], fontsize=12)
    
    #4.2 More Chance
    ax2.set_xlabel('Chest Pain Type', fontsize=14)
    ax2.set_ylabel('Count', fontsize=14)
    ax2.set_title('More Chance', fontsize=16)
    ax2.legend(title='Sex', labels=['Female', 'Male'], fontsize=12)
    
    # remove the top and right spines from each subplot
    sns.despine(ax=ax1)
    sns.despine(ax=ax2)
    
    # set the x-tick labels for the chest pain types
    for ax in [ax1, ax2]:
        ax.set_xticklabels(['typical angina','atypical angina','non-anginal pain','asymptomatic'], fontsize=12, rotation=45, ha='right')
    
    # set the title
    plt.suptitle('Chest Pain Type by Sex and Heart Disease Status', fontsize=18, fontweight='bold')
        
    # show the plot
    st.pyplot(fig)

#5. Fasting Blood Sugar by Sex and Heart Disease Status
if '5. Fasting Blood Sugar by Sex and Heart Disease Status' in selected_options:
    st.subheader('5. Fasting Blood Sugar by Sex and Heart Disease Status')
    palette = sns.color_palette(['#1f77b4', '#2ca02c'])
    sns.set_style("whitegrid")
    sns.set_palette(palette)
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 6))
    
    sns.countplot(x=data[data['target']==0]['fbs'], hue=data[data['target']==0]['sex'], palette=palette, ax=ax1)
    sns.countplot(x=data[data['target']==1]['fbs'], hue=data[data['target']==1]['sex'], palette=palette, ax=ax2)
    
    #5.1 Less Chance
    ax1.set_xlabel('Fasting Blood Sugar', fontsize=14)
    ax1.set_ylabel('Count', fontsize=14)
    ax1.set_title('Less Chance', fontsize=16)
    ax1.legend(title='Sex', labels=['Female', 'Male'], fontsize=12)
    
    #5.2 More Chance
    ax2.set_xlabel('Fasting Blood Sugar', fontsize=14)
    ax2.set_ylabel('Count', fontsize=14)
    ax2.set_title('More Chance', fontsize=16)
    ax2.legend(title='Sex', labels=['Female', 'Male'], fontsize=12)
    
    sns.despine(ax=ax1)
    sns.despine(ax=ax2)
    
    # set the x-tick labels for the fasting blood sugar values
    for ax in [ax1, ax2]:
        ax.set_xticklabels(['<120mg/dl','>120 mg/dl'], fontsize=12, rotation=45, ha='right')
    
    # set the title
    plt.suptitle('Fasting Blood Sugar by Sex and Heart Disease Status', fontsize=18, fontweight='bold')
    st.pyplot(fig)

#6. Resting Blood Sugar by Sex and Heart Disease Status
if '6. Resting Blood Sugar by Sex and Heart Disease Status' in selected_options:
    st.subheader('6. Resting Blood Sugar by Sex and Heart Disease Status')
    palette = sns.color_palette(['#1f77b4', '#2ca02c'])
    sns.set_style("whitegrid")
    sns.set_palette(palette)
    
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 6))
    
    sns.kdeplot(data[data['target']==0][data['sex']==0]['trestbps'], shade=True, ax=ax1, label='Female')
    sns.kdeplot(data[data['target']==0][data['sex']==1]['trestbps'], shade=True, ax=ax1, label='Male')
    sns.kdeplot(data[data['target']==1][data['sex']==0]['trestbps'], shade=True, ax=ax2, label='Female')
    sns.kdeplot(data[data['target']==1][data['sex']==1]['trestbps'], shade=True, ax=ax2, label='Male')
    
    #6.1 Less Chance
    ax1.set_xlabel('Resting Blood Pressure', fontsize=14)
    ax1.set_ylabel('Density', fontsize=14)
    ax1.set_title('Less Chance', fontsize=16)
    ax1.legend(title='Sex', fontsize=12)
    
    #6.2 Less Chance
    ax2.set_xlabel('Resting Blood Pressure', fontsize=14)
    ax2.set_ylabel('Density', fontsize=14)
    ax2.set_title('More Chance', fontsize=16)
    ax2.legend(title='Sex', fontsize=12)
    
    sns.despine(ax=ax1)
    sns.despine(ax=ax2)
    
    # set the title
    plt.suptitle('Resting Blood Pressure by Sex and Heart Disease Status', fontsize=18, fontweight='bold')
    st.pyplot(fig)

#7. Cholesterol Level by Sex and Heart Disease Status
if '7. Cholesterol Level by Sex and Heart Disease Status' in selected_options:
    
    st.subheader('7. Cholesterol Level by Sex and Heart Disease Status')
    palette = sns.color_palette(["#7FB3D5", "#2C5F2D"])
    
    sns.set_style("whitegrid")
    sns.set_palette(palette)
    
    # create a figure and axis object with two subplots
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 6))
    
    # create the KDE plots for target = 0 and target = 1
    sns.kdeplot(x=data[data['target']==0][data['sex']==0]['chol'], shade=True, label='Female', ax=ax1)
    sns.kdeplot(x=data[data['target']==0][data['sex']==1]['chol'], shade=True, label='Male', ax=ax1)
    sns.kdeplot(x=data[data['target']==1][data['sex']==0]['chol'], shade=True, label='Female', ax=ax2)
    sns.kdeplot(x=data[data['target']==1][data['sex']==1]['chol'], shade=True, label='Male', ax=ax2)
    
    #7.1 Less Chance
    ax1.set_xlabel('Cholesterol Level', fontsize=14)
    ax1.set_ylabel('Density', fontsize=14)
    ax1.set_title('Less Chance', fontsize=16)
    ax1.legend(title='Sex', fontsize=12)
    
    #7.2 More Chance
    ax2.set_xlabel('Cholesterol Level', fontsize=14)
    ax2.set_ylabel('Density', fontsize=14)
    ax2.set_title('More Chance', fontsize=16)
    ax2.legend(title='Sex', fontsize=12)
    
    # remove the top and right spines from each subplot
    sns.despine(ax=ax1)
    sns.despine(ax=ax2)
    
    # set the title
    plt.suptitle('Cholesterol Level by Sex and Heart Disease Status', fontsize=18, fontweight='bold')
    st.pyplot(fig)
