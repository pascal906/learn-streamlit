import streamlit as st

st.title("This is the title of the app")

st.header("This is the header")

st.subheader("This is the subheader")

st.text("This is normal text, or text data")

st.write("This is default font, to write output to app")

# markdown

st.markdown("This is markdown")

# heading
st.markdown("# This is heading 1 markdown")
st.markdown("## This is heading 2 markdown")
st.markdown("### This is heading 3 markdown")
# and so on

# bold
st.markdown("This text is **bold**")
# italic
st.markdown("This text is *italic*")

# put a link
st.markdown("[Markdown Cheatsheet](https://www.markdownguide.org/cheat-sheet/)")

# a list
st.markdown(
    """
    1. satu
    2. dua
    3. tiga

    or

    - satu
    - dua
    - tiga
    """
)

# code markdown
st.markdown(
    """
    `print("Hello, world!")`
    """
)

# emoji
st.markdown("[Emojis](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/)")
st.markdown(":smile:")