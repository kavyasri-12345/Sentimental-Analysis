import streamlit as st
import pickle

# Load model
model = pickle.load(open('best_model.pkl', 'rb'))

# Streamlit UI
st.title("Sentiment Analysis")
text = st.text_area("Enter a review:")
if st.button("Analyze"):
    prediction = model.predict([text])
    st.write(f"Sentiment: {prediction[0]}")
