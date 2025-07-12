import streamlit as st

st.write("Hello, *World!* :sunglasses:")

st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.title("_Streamlit_ is :blue[cool] :sunglasses:")

st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")

st.markdown("*Streamlit* is **really** ***cool***.")

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
