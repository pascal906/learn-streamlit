import streamlit as st

# interactive widgets
st.title("Streamlit interactive widgets examples")

# button
button = st.button("Click Me")
if button:
	st.write("You click me!")

# checkbox 
checkbox = st.checkbox("Check me to enable!")
if checkbox:
	st.write("Checkbox is  clicked")

# radio button
radio = st.radio("Choose an option: ", ["2011", "2011", "All"])
st.write("You have selected: ", radio)

# selectbox
selectbox = st.selectbox("Choose an option: ", ["2011", "2012", "All"]*2)
st.write("You have selected: ", selectbox)

# multiselect
multiselect = st.multiselect("Choose multiple items: ", ["2011", "2012", "All"])
st.write("Your selection is: ", multiselect)

# range slider
rating = st.slider("Select your rating", min_value=1.0, max_value=5.0, step=0.5)
st.write("Your rating is: ", rating)

# slider, but select
select_slider = st.select_slider("Select a value", ["2011", "2012", "All"])