import streamlit as st
import pandas as pd
import joblib
import numpy as np
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import matplotlib.pyplot as plt

# Layout and Title
st.set_page_config(page_title="HR Attrition Predictor", layout="wide")
st.markdown("<h1 style='text-align:center;'>🧠 HR Attrition Risk Predictor + LLM Agent</h1>", unsafe_allow_html=True)

# Load Assets
model = joblib.load("best_model.pkl")
encoder = joblib.load("encoder.pkl")
shap_values = np.load("shap_values.npy", allow_pickle=True)

# Email config
SENDER_EMAIL = "rohitbhagasra4@gmail.com"
SENDER_PASSWORD = "uinikxehmairbpei"
HR_EMAIL = "roxhiit4@gmail.com"

# Email Function
def notify_hr_email(subject, body, to_email):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        st.error(f"❌ Email failed: {e}")
        return False

# LLM Integration
def get_llm_response(prompt):
    try:
        response = requests.post(
            "http://localhost:1234/v1/chat/completions",
            headers={"Content-Type": "application/json"},
            json={
                "model": "qwen3-8b",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
            }
        )
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ LLM not responding: {e}"

# Upload
uploaded_file = st.file_uploader("📂 Upload Employee CSV File", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully.")
    st.dataframe(df.head())

    if "Churn" in df.columns:
        df.drop(columns=["Churn"], inplace=True)

    feature_names = df.columns.tolist()
    df_encoded = encoder.transform(df)

    # Sidebar
    st.sidebar.header("📊 Employee Dashboard")
    st.sidebar.markdown(f"👥 **Total Employees:** {len(df)}")
    dept_filter = st.sidebar.multiselect("Filter by Department", options=df["Department"].unique())
    if dept_filter:
        df = df[df["Department"].isin(dept_filter)]
        df_encoded = encoder.transform(df)

    if st.button("🔍 Analyze Attrition Risk"):
        risk_rows, recommendations, risk_probabilities = [], [], []

        for i in range(df_encoded.shape[0]):
            input_processed = df_encoded[i].reshape(1, -1)
            proba = model.predict_proba(input_processed)[0][1]

            if proba >= 0.5:
                shap_row = shap_values[i]
                top_indices = np.argsort(np.abs(shap_row))[-3:][::-1]

                try:
                    reasons = ", ".join(
                        f"🔸 **{feature_names[int(j)]}**: {df.iloc[i, int(j)]}"
                        for j in top_indices if int(j) < len(feature_names)
                    )
                except:
                    reasons = "⚠️ Could not extract SHAP reasons."

                prompt = f"""
                You are an HR assistant.
                The employee is predicted to leave the company.
                The top contributing factors are: {reasons}.
                Suggest 2–3 actionable HR interventions to help retain this employee.
                """
                answer = get_llm_response(prompt)

                risk_rows.append(df.iloc[i])
                recommendations.append(answer)
                risk_probabilities.append(proba)

                with st.expander(f"🔴 Employee {i+1} at Risk (🔥 {proba:.2f})", expanded=False):
                    st.write("**🚨 Top Risk Factors:**", reasons)
                    st.markdown("**💡 LLM Recommendations:**")
                    st.info(answer)
                    st.progress(proba)

                    if st.button(f"📩 Notify HR for Employee {i+1}"):
                        subject = f"🚨 Attrition Alert: Employee {i+1}"
                        body = f"""
                        Employee {i+1} is predicted to leave.
                        Risk Factors: {reasons}

                        LLM Suggestions:
                        {answer}
                        """
                        if notify_hr_email(subject, body, HR_EMAIL):
                            st.success("✅ Email sent to HR!")

        # Summary
        st.sidebar.markdown(f"❗ **At-Risk:** {len(risk_rows)}")
        st.sidebar.markdown(f"✅ **Safe:** {len(df) - len(risk_rows)}")

        # Department Chart
        if "Department" in df.columns and risk_rows:
            st.subheader("📊 At-Risk Employees by Department")
            risk_df = pd.DataFrame(risk_rows)
            chart_data = risk_df["Department"].value_counts()
            fig, ax = plt.subplots()
            chart_data.plot(kind="bar", color="crimson", ax=ax)
            ax.set_xlabel("Department")
            ax.set_ylabel("Count")
            ax.set_title("At-Risk Count by Department")
            st.pyplot(fig)

        # Downloadable CSV
        if risk_rows:
            final_df = pd.DataFrame(risk_rows)
            final_df["Attrition Probability"] = risk_probabilities
            final_df["LLM Recommendation"] = recommendations
            csv = final_df.to_csv(index=False).encode()
            st.download_button(
                label="⬇️ Download At-Risk Employees CSV",
                data=csv,
                file_name="at_risk_employees.csv",
                mime="text/csv"
            )

# Contact Info
with st.sidebar:
    st.markdown("---")
    st.markdown("💬 **Need HR Help?**")
    st.markdown("[📧 Email Us](mailto:roxhiit4@gmail.com)")
    st.markdown("[💬 WhatsApp](https://wa.me/918595927256)")
