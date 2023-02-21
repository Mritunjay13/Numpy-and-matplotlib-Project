import streamlit as st
import time
st.title('Hello! This is my first app.')
st.header('This is the header')
st.markdown('Description as markdown')
st.subheader('This is subheading')
st.caption('My caption')
st.code('d=[1,2,3] print(d)')
st.image("https://images.ctfassets.net/pdf29us7flmy/4FaqpZFMenRQoDl0LGqFes/02c40a20ee37917f3e117b9c599f132d/GOLD-6487-CareerGuide-Batch04-Images-GraphCharts-01-Line.png")


#Widgets

st.checkbox('Male')
st.checkbox('Female')
st.button('Click')
st.radio('Seleect the scale',['Feet','Meter','cm'])
st.selectbox('Select the city',['Mumbai','Delhi','Kolkata'])
st.multiselect('Select the city',["A",'B','C'])
st.slider('Select the range of weight',0,100)
st.select_slider('Pick your rating',['Bad','Good','Average','Excelent'])
st.number_input('Give us a rating 1-10',0,10)
st.text_input('Please enter your name')
st.date_input('Enter the date as we served you')
st.time_input('enter the time')
st.text_area('Write your feedback here')
st.file_uploader('upload the csv')
st.color_picker('Choose your colour')
st.subheader('Progress bar')
a=5
while a<=100:
    with st.progress(a):
        a=a+5
    time.sleep(10)

st.subheader('Process undergoing ... please wait!')
with st.spinner('Wait...'):
    time.sleep(10)