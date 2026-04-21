import streamlit as st

st.title("🫀 Heart Disease Prediction System")

st.image(
    "https://static.vecteezy.com/system/resources/previews/002/557/047/non_2x/heartbeat-line-illustration-pulse-trace-ecg-or-ekg-cardio-graph-symbol-for-healthy-and-medical-analysis-illustration-vector.jpg",
    width=400
)

st.markdown("<h3 style='text-align:center;color:gray;'>Machine Learning Based Heart Risk Prediction</h3>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; font-size:18px;'>
Predict heart disease risk using patient health data and machine learning models.
</div>
""", unsafe_allow_html=True)
st.markdown("""
## 💡 Welcome!

This app helps you:

✔ Predict heart disease risk  
✔ Get health tips  
✔ Track your history  

---

## 🚀 How to use:

1. Go to 👉 Prediction page  
2. Enter details  
3. Click Predict  
4. View Dashboard  

---

Stay healthy ❤️
""")