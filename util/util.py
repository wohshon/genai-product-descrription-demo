import streamlit as st


def sidebar(page):
    with st.sidebar:
        if page == 'product_description':
            st.divider
            st.markdown("### How to use this demo")
            st.write("Enter a product name in the text box, press Enter to submit")
            st.write("A sample prompt will be generated in the text area, feel free to edit the prmppt for experimentation ")
            st.write(" ")
            st.write("** Some fringe cases may run into parsing errors (occurring at langchain), currently the demo does not filter out those cases, if any error is encountered, simply re-submit the query")
