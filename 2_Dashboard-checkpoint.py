import plotly.express as px
import pandas as pd
from datetime import datetime
import streamlit as st
import matplotlib.pyplot as plt

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


st.title("📊 Advanced Dashboard")
st.success("📊 Real-time analytics dashboard with trend and timeline insights")

if "history" in st.session_state and len(st.session_state.history) > 0:
    risks = [item["Risk %"] for item in st.session_state.history]

    col1, col2, col3 = st.columns(3)

    with col1:
      st.metric("📊 Total Predictions", len(risks))

    with col2:
      st.metric("📉 Avg Risk", round(sum(risks)/len(risks),2))

    with col3:
      st.metric("🚨 Max Risk", max(risks))


    fig, ax = plt.subplots()
    ax.grid(True)
    ax.set_facecolor("#f9f9f9")
    ax.plot(risks, marker='o')
    ax.set_xlabel("Prediction Number")
    ax.set_ylabel("Risk %")
    ax.set_title("Risk Trend")
    st.pyplot(fig)


    fig2, ax2 = plt.subplots()
    ax2.bar(range(len(risks)), risks)
    ax2.set_xlabel("Prediction Number")
    ax2.set_ylabel("Risk %")
    st.pyplot(fig2)
    
    tab1, tab2 = st.tabs(["📈 Trends", "📊 Distribution"])

    with tab1:
       st.markdown("### 📈 Risk Trend Over Time")
       st.pyplot(fig)

    with tab2:
       st.markdown("### 📊 Risk Distribution")
       st.pyplot(fig2)

    st.markdown("---")

    st.markdown("### 📊 Interactive Risk Timeline")

    if "history" not in st.session_state:
       st.session_state.history = []

    if len(st.session_state.history) == 0:
       st.info("No predictions yet. Make a prediction first 👇")
    else:

       df = pd.DataFrame(st.session_state.history)

       fig3 = px.line(
          df,
          x="Time",
          y="Risk %",
          markers=True,
          title="Risk Trend Over Time"
       )

       st.plotly_chart(fig3, use_container_width=True)

    