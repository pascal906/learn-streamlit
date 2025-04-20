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

# topic 1 part2
st.markdown("### HTML")
html_code = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            body {boackground-color: powderblue;}
            h1 {color: blue;}
            p {color: red;}
        </style>
    </head>
    <body>
        <h1>This is a heading</h1>
        <p>This is a paragraph.</p>
    </body>
</html>
"""

st.markdown(html_code, unsafe_allow_html=True)

# create a divide
st.markdown("---")

# or use
st.write("this is another divider")
st.divider()

# latex
# https://www.overleaf.com/learn/latex/Mathematical_expressions
st.markdown("## Latex code")
st.subheader("Einstein Equation")
st.latex("E = mc^2")
st.write("Another equation")
st.latex("x^2 + y^2 = z^2")
st.latex("y = \sqrt{2^2+1}")
st.latex(r"g(x) = \frac{1}{x^2+y^3}")
