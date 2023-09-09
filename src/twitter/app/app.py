import streamlit as st
from twitter.components.model_predictor import predict

st.title("Sentiment Analyzer")

text=st.text_input("Write Your text here",max_chars=100)

if st.button("Analyze")==True:
    arg=predict(text)
    if arg==0:
        st.markdown("## Negative")
    if arg==1:
        st.markdown("## Neutral")
    if arg==2:
        st.markdown("## Positive")




