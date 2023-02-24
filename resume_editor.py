import os

import streamlit as st

st.set_page_config(page_title='Resume_builder',layout="wide")
hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                header {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.header("RESUME EDITOR")


def edit():
    with st.expander("Admin portal"):
        st.subheader("Edit your files in this format")
        with open("help.txt",'r') as source:
            st.code(source.read())
        for file in os.listdir():
            if(".txt" in file and file != 'requirements.txt' and file != 'help.txt'):
                with open(file,'r') as f:
                    value = st.text_area("Update " + file,f.read())
                    f.close()
                if(st.button('Save ' + file)):
                    with open(file,'w') as f:
                        f.write(value)
                        f.close()
                    st.success("Saved successfully")


st.sidebar.header("Admin login")
id = st.sidebar.text_input("Enter login id: ")
password = hash(st.sidebar.text_input("Enter password: ",type="password"))
true_password = hash("PassFile@2023#")
if(id and password):
    if(id.lower() == "admin" and password == true_password):
        st.sidebar.success("Log in successfull")
        edit()
    else:
        st.error("Incorrect id or password")