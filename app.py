import streamlit as st
import pickle


with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("📩 Spam Message Predictor")


user_input = st.text_area("Enter your message:")


if st.button("🔍 Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message before predicting.")
    else:
        prediction = model.predict([user_input])[0]
        print(prediction)
        label = "🚫 SPAM" if prediction == 1 else "✅ HAM (Not Spam)"
        st.subheader(f"Prediction: {label}")
