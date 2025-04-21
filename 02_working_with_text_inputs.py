import streamlit as st
# belajar cara menangani text input pada streamlit

st.header("Text inputs handling")

# text input, untuk membuatnya,
# kita perlu membuat variabel tempat menyimpan nilai inputan
name = st.text_input("Enter your name:")

# text area input, multiline, and longer than text input
feedback = st.text_area("Enter your feedback:")

age = st.number_input("Enter your age:")

date = st.date_input("Select a date")

time = st.time_input("Pick a time")

color = st.color_picker("Pick a color")

# display input:
st.write("Name: ", name)
st.write("Feedback: ", feedback)
st.write("Age: ", age)
st.write("Date: ", date)
st.write("Time: ", time)
st.write("Color: ", color)

# dynamicly change color
html_code = """
<h1 style="color:{};">This is a heading</h1>
<p style="color:aqua;">This is a paragraph.</p>
""".format(color)

st.markdown(html_code, unsafe_allow_html=True)