# 🧠 HR Attrition Risk Predictor + LLM Agent

This project is a smart Human Resource analytics system that integrates **Machine Learning (ML)** and a **Large Language Model (LLM)** to proactively predict employee attrition and provide **actionable HR recommendations**. It helps HR professionals retain key employees by combining data science and AI reasoning.

---

## 🚀 Key Features

- 🔍 **Attrition Prediction**  
  Uses machine learning classification models to predict whether an employee is likely to leave.

- 📊 **SHAP Explainability**  
  Visualizes which features contributed most to each prediction for transparency.

- 💡 **LLM-Powered Recommendations**  
  Connects to a local LLM (Qwen 3B via LM Studio) to suggest HR interventions for at-risk employees.

- 📩 **HR Email Notifications**  
  Automatically sends an email to HR for high-risk cases with insights and suggestions.

- 📁 **CSV Upload & Filtering**  
  Upload structured employee data and filter by department to view focused results.

- ⬇️ **Downloadable Reports**  
  Export a CSV of all at-risk employees along with LLM recommendations and risk probability.

---

## 🛠️ Technologies Used

| Layer         | Tools/Frameworks                                |
|---------------|--------------------------------------------------|
| **Frontend**  | Streamlit                                        |
| **ML Model**  | Scikit-learn (Random Forest / XGBoost)           |
| **LLM Agent** | Qwen3B via LM Studio (Local API)                 |
| **Explainability** | SHAP                                  |
| **Email Alerts** | SMTP + Gmail API                        |
| **Data Tools** | Pandas, NumPy, Matplotlib, Joblib              |

---

▶️How to Run Locally
bash
Copy
Edit
# 1. Clone the Repository
git clone https://github.com/Rohittyogii/Predictive-Model-Actionable-Agent-for-Project-Risk
cd Predictive-Model-Actionable-Agent-for-Project-Risk

# 2. Install Dependencies
pip install -r requirements.txt

# 3. Start the Streamlit App
streamlit run Streamlit.py
Once the app launches in your browser:

1. Upload an employee CSV file (example_data.csv structure).

2.Click "Analyze Attrition Risk" to predict and generate recommendations.

3. Optionally, notify HR with just one click via email.

📌 Use Case & Impact
In large organizations, predicting employee churn in advance is essential. This project:

✅ Identifies at-risk employees using data
✅ Explains why they are at risk using SHAP
✅ Provides HR intervention plans via LLM
✅ Notifies the HR team instantly by email


📬 Contact
Project by: Rohit Kumar
📧 Email: roxhiit4@gmail.com
🔗 GitHub: github.com/Rohittyogii

