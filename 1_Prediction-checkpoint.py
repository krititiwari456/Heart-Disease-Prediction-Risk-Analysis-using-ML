import streamlit as st
import numpy as np
import pickle

st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
h1, h2, h3 {
    color: #222;
    text-align: center;
}
.stMetric {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# Multiple users
users = {
    "user1": "123",
    "user2": "456",
    "admin": "admin123"
}

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if username not in users or users[username] != password:
    st.warning("Invalid login")
    st.stop()
else:
    st.sidebar.success(f"Welcome {username}")
    st.sidebar.title("ℹ️ Info")
    st.sidebar.info("This app predicts heart disease risk using Machine Learning.")
# Load model
model = pickle.load(open("model.pkl", "rb"))


# Title
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    h1 {
        color: #ff4b4b;
        text-align: center;
        font-family: 'Arial Black';
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-size: 18px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown("<h1>🫀 Heart Disease Prediction System</h1>", unsafe_allow_html=True)
st.write("Enter patient details below:")

# Input fields
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, key="age")
    sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1], key="sex")
    cp = st.selectbox("Chest Pain Type (0-3)", [0,1,2,3], key="cp")
    trestbps = st.number_input("Resting Blood Pressure", key="trestbps")
    chol = st.number_input("Cholesterol", key="chol")
    fbs = st.selectbox("Fasting Blood Sugar > 120", [0,1], key="fbs")

with col2:
    restecg = st.selectbox("Rest ECG (0-2)", [0,1,2], key="restecg")
    thalach = st.number_input("Max Heart Rate", key="thalach")
    exang = st.selectbox("Exercise Induced Angina", [0,1], key="exang")
    oldpeak = st.number_input("Oldpeak", key="oldpeak")
    slope = st.selectbox("Slope (0-2)", [0,1,2], key="slope")
    ca = st.selectbox("Number of Major Vessels (0-3)", [0,1,2,3], key="ca")
    thal = st.selectbox("Thal (1-3)", [1,2,3], key="thal")

if st.button("Predict"):

    input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                            restecg, thalach, exang, oldpeak,
                            slope, ca, thal]])
    
    st.subheader("Prediction Result")
    st.markdown("---")
    
    if st.button("🔄 Reset"):
      st.session_state.clear()


    if age == 0 or trestbps == 0 or chol == 0:
      st.error("⚠️ Please fill all required fields properly")
      st.stop()
    
    # Prediction
    st.subheader("🧾 Patient Summary")

    st.write(f"Age: {age}, BP: {trestbps}, Cholesterol: {chol}")
    prediction = model.predict(input_data)

    # Probability
    probability = model.predict_proba(input_data)[0][1]
    risk_percentage = round(probability * 100, 2)
    st.progress(int(risk_percentage))

    st.subheader("Prediction Result")
    st.markdown(f"""
    <div style="
    background-color:#ffffff;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 0px 10px rgba(0,0,0,0.1);
    text-align:center;
    ">
    <h2>🧠 Risk Percentage</h2>
    <h1 style='color:red;'>{risk_percentage}%</h1>
    </div>
    """, unsafe_allow_html=True)

    health_score = 100 - risk_percentage
    # Color logic
    if health_score > 70:
      color = "green"
    elif health_score > 40:
      color = "orange"
    else:
      color = "red"

    st.markdown(f"""
    <div style="
    background-color:#e8f5e9;
    padding:15px;
    border-radius:10px;
    text-align:center;
    ">
    <h3>💚 Health Score</h3>
    <h2 style='color:{color};'>{health_score}/100</h2>
    </div>
    """, unsafe_allow_html=True)

    if risk_percentage < 30:
      st.markdown("🟢 **Low Risk**")
    elif risk_percentage < 60:
      st.markdown("🟡 **Medium Risk**")
    else:
      st.markdown("🔴 **High Risk**")
    
    
    st.subheader("🔮 Future Risk Simulation")
    st.markdown("---")
    # Simulate improved conditions
    improved_chol = chol - 40
    improved_bp = trestbps - 20
    improved_oldpeak = oldpeak - 1

    # Avoid negative values
    improved_chol = max(improved_chol, 100)
    improved_bp = max(improved_bp, 80)
    improved_oldpeak = max(improved_oldpeak, 0)

    # New input with improved values
    improved_data = np.array([[age, sex, cp, improved_bp, improved_chol, fbs,
                          restecg, thalach, exang, improved_oldpeak,
                          slope, ca, thal]])

    # Predict new risk
    new_prob = model.predict_proba(improved_data)[0][1]
    new_risk = round(new_prob * 100, 2)

    st.write(f"Current Risk: {risk_percentage}%")
    st.write(f"After Lifestyle Improvement: {new_risk}%")

    st.subheader("🧠 Why this prediction?")

    reasons = []

    if chol > 240:
      reasons.append("High cholesterol is increasing your risk")

    if trestbps > 140:
      reasons.append("High blood pressure detected")

    if thalach < 120:
      reasons.append("Low heart rate may indicate poor heart health")

    if oldpeak > 2:
      reasons.append("High stress level (oldpeak) detected")

    if len(reasons) > 0:
      for r in reasons:
         st.warning("⚠️ " + r)
    else:
      st.success("No major risk factors detected 👍")

    st.subheader("🏥 Suggested Action")

    if risk_percentage > 70:
      st.error("Consult a Cardiologist Immediately")
    elif risk_percentage > 40:
      st.warning("Schedule a medical checkup soon")
    else:
      st.success("Maintain healthy lifestyle")

    avg_risk = 45  # approx dataset avg

    st.subheader("📊 Comparison")

    if risk_percentage > avg_risk:
      st.error("Your risk is above average")
    else:
      st.success("Your risk is below average")


    st.markdown("---")
    st.subheader("💡 Personalized Health Tips")

    tips = []

    if chol > 240:
      tips.append("Reduce oily and fatty foods")

    if trestbps > 140:
      tips.append("Reduce salt intake and manage stress")

    if thalach < 120:
      tips.append("Engage in regular cardio exercise")

    if oldpeak > 2:
      tips.append("Consult doctor for heart stress management")
    if age > 55:
      tips.append("Regular heart checkups recommended")

    if exang == 1:
      tips.append("Avoid heavy physical stress and consult doctor")

    if len(tips) > 0:
      for t in tips:
        st.write("•", t)
    else:
      st.write("You are maintaining good health 👍")

    import pandas as pd

    data = pd.DataFrame([{
      "Age": age,
      "Risk %": risk_percentage
    }])

    csv = data.to_csv(index=False)

    st.download_button(
    label="⬇ Download Data (CSV)",
    data=csv,
    file_name="report.csv",
    mime="text/csv"
    )

    # Suggestion
    if new_risk < risk_percentage:
      st.success("🎉 Risk can be reduced by improving lifestyle!")
    else:
      st.warning("⚠️ Minor improvement, regular monitoring needed.")
    
    import matplotlib.pyplot as plt

    st.subheader("Risk Distribution")

    labels = ["Risk", "Safe"]
    sizes = [risk_percentage, 100 - risk_percentage]
    colors = ["red", "green"]

    fig, ax = plt.subplots()
    ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    colors=colors,
    startangle=90
    )
    ax.axis('equal')

    st.pyplot(fig)
    
    st.subheader("Risk Distribution")
    st.markdown("---")
   
    # Result logic
    if risk_percentage < 30:
     st.success("✅ Low Risk")
     st.info("💡 Maintain a healthy lifestyle, exercise regularly, and eat balanced food.")
    
    elif risk_percentage < 60:
     st.warning("⚠️ Medium Risk")
     st.info("💡 Monitor your health, reduce stress, and consult a doctor if needed.")
    
    else:
     st.error("🚨 High Risk")
     st.info("💡 Immediate medical attention recommended. Consult a cardiologist.")

    # Save history
    from datetime import datetime

    if "history" not in st.session_state:
      st.session_state.history = []

    st.session_state.history.append({
      "Age": age,
      "Risk %": risk_percentage,
      "Time": datetime.now().strftime("%d-%m-%Y %H:%M")
    })
    
    st.subheader("Prediction History")
    if "history" in st.session_state:
      st.table(st.session_state.history)

    from reportlab.platypus import SimpleDocTemplate, Paragraph
    from reportlab.lib.styles import getSampleStyleSheet
    import io

    # Create PDF in memory
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("Heart Disease Prediction Report", styles['Title']))
    content.append(Paragraph(f"Age: {age}", styles['Normal']))
    content.append(Paragraph(f"Risk Percentage: {risk_percentage}%", styles['Normal']))

    if risk_percentage < 30:
     result = "Low Risk"
    elif risk_percentage < 60:
     result = "Medium Risk"
    else:
     result = "High Risk"

    content.append(Paragraph(f"Result: {result}", styles['Normal']))

    content.append(Paragraph("Recommendations:", styles['Heading2']))

    for t in tips:
      content.append(Paragraph(f"- {t}", styles['Normal']))
    
    doc.build(content)
    
    from datetime import datetime

    content.append(Paragraph(f"Date: {datetime.now()}", styles['Normal']))

    # Download button
    st.download_button(
    label="📄 Download Report",
    data=buffer,
    file_name="heart_report.pdf",
    mime="application/pdf"
    )
