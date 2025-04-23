# disini kita akan belajar tentang status dan progess indicators
# import library
import streamlit as st
import time

# title
st.title("Status and Progress Indicators Examples")

# empty element
empty = st.empty()
empty.text("This text will be replaced after 5 seconds")

time.sleep(1)
empty.text("This is new text data")

# progress bar
progress = st.progress(0)
status_text = st.empty()

for i in range(101):
    time.sleep(0.01)
    progress.progress(i)
    status_text.text("Progress: {}".format(i))
status_text.text("Progress: Done!")

# spinner

with st.spinner("Waiting..."):
    time.sleep(5)
    
    # load large file here
st.success("Process is Done!")
st.warning("This is warning message!")
st.error("This is error!")
st.info("This is information!")


# decoration
st.snow()

# theres also:
st.balloons()