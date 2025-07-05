# 🧠 HR Attrition Risk Predictor + LLM Agent

This project is a smart HR analytics tool that uses Machine Learning and a Language Model Agent (LLM) to **predict employee attrition risk** and provide **actionable HR recommendations**.

## 🚀 Features

- 🔍 **Attrition Prediction**: Predict whether an employee is at risk of leaving using ML classification models.
- 📈 **SHAP Explainability**: Shows top features influencing each prediction using SHAP values.
- 💡 **LLM Agent**: Suggests HR actions for at-risk employees based on key contributing factors.
- 📩 **HR Email Notifications**: Instantly notify HR via email for any high-risk cases.
- 📊 **Department-wise Visualization**: See attrition risk by department.
- 📁 **CSV Upload & Download**: Upload employee data and download at-risk reports.

---

## 🛠️ Technologies Used

- **Frontend**: Streamlit
- **ML Model**: Scikit-learn (Random Forest / XGBoost / etc.)
- **LLM API**: Open-source model (e.g., Qwen/Q&A endpoint)
- **Explainability**: SHAP
- **Email Service**: SMTP + Gmail
- **Others**: Pandas, NumPy, Matplotlib

---

## 📁 Project Structure

.
├── Streamlit.py           # Streamlit UI code (Frontend & LLM integration)
├── generate_models.py     # Python script to train the ML model and save artifacts
├── best_model.pkl         # Trained machine learning model
├── encoder.pkl            # OneHotEncoder used during training
├── shap_values.npy        # SHAP values used to interpret model predictions
├── example_data.csv       # Sample employee dataset for testing
├── README.md              # Project documentation (this file)
├── requirements.txt       # List of required Python packages
├── agent_flow.png         # Agent flow diagram (optional)
└── screenshots/           # Folder with UI and result screenshots (optional)



---

## ▶️ How to Run Locally

1. **Clone the repository**  
   ```bash
   git clone (https://github.com/Rohittyogii/Predictive-Model-Actionable-Agent-for-Project-Risk)
   cd Predictive-Model-Actionable-Agent-for-Project-Risk

Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
Run Streamlit app

bash
Copy
Edit
streamlit run Streamlit.py
Upload a CSV file with employee details to get predictions and recommendations.
