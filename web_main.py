import streamlit as st
st.markdown(
    "<h1 style='text-align: center;'>SMS Classifier</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<div style='text-align: center; font-size: 20px; margin-top: -10px;'>A simple web app to classify SMS messages as spam or ham.</div><br>",
    unsafe_allow_html=True
)
st.divider()
txt = st.text_area("Enter your SMS message here:", height=150)
st.button("Classify Message")
st.markdown(
    "<div style='text-align: center; margin-top: 20px; color: gray;'>Developed by Your Subal Kundu</div>",
    unsafe_allow_html=True
)