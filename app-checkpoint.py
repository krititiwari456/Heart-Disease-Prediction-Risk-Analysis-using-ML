import streamlit as st


st.markdown("""
<style>
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    font-size: 18px;
    border-radius: 10px;
}

.stTextInput, .stNumberInput {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Heart Disease App", layout="wide")

st.markdown("<h1 style='text-align:center;'>🫀 Heart Disease Prediction System</h1>", unsafe_allow_html=True)

st.markdown("## 👋 Welcome!")

st.info("This application helps in predicting heart disease risk using Machine Learning.")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("🔍 Easy Prediction")

with col2:
    st.warning("📊 Visual Insights")

with col3:
    st.info("💡 Health Tips")

st.markdown("---")

st.markdown("### 🚀 How to Use")
st.write("""
1. Go to Prediction page  
2. Enter patient details  
3. Click Predict  
4. View results and analysis  
""")







