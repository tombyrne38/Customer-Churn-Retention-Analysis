
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction")

st.markdown(
    """
    Estimate a customer's likelihood of leaving using a
    machine learning model trained on the IBM Telco Customer Churn dataset.

    **How to use:** Enter the customer's details below,
    then click **Predict Churn Risk** to view their estimated
    churn probability and risk classification.
    """
)

st.write(
    "An interactive machine learning application "
    "for exploring customer churn risk."
)

st.info(
    "This application is a portfolio demonstration "
    "and does not provide live business predictions."
)


@st.cache_resource
def load_model():
    return joblib.load("churn_prediction_model.joblib")

model = load_model()

st.success("Machine learning model loaded successfully!")


st.header("Customer Information")

st.subheader("Customer Details")

col1, col2 = st.columns(2)
with col1:
    tenure = st.slider(
    "Customer tenure (months)",
    min_value=0,
    max_value=72,
    value=12
)

with col2:
    contract = st.selectbox(
    "Contract type",
    ["Month-to-month", "One year", "Two year"]
)




st.subheader("Personal & Account Details")

gender = st.selectbox("Gender", ["Female", "Male"])

senior_citizen = st.selectbox(
    "Senior citizen",
    ["No", "Yes"]
)

partner = st.selectbox("Partner", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])

paperless_billing = st.selectbox(
    "Paperless billing",
    ["No", "Yes"]
)

st.subheader("Billing & Payment")

charges_col1, charges_col2 = st.columns(2)
with charges_col1:
    monthly_charges = st.number_input(
    "Monthly charges (currency units)",
    min_value=0.0,
    max_value=200.0,
    value=70.0,
    step=1.0
)
with charges_col2:
    total_charges = st.number_input(
    "Total charges (currency units)",
    min_value=0.0,
    value=840.0,
    step=10.0
)

payment_method = st.selectbox(
    "Payment method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

st.subheader("Phone & Internet Services")

phone_col1, phone_col2 = st.columns(2)

with phone_col1:
    phone_service = st.selectbox(
        "Phone service",
        ["No", "Yes"]
    )

with phone_col2:
    if phone_service == "No":
        multiple_lines = st.selectbox(
            "Multiple lines",
            ["No phone service"],
            disabled=True
        )
    else:
        multiple_lines = st.selectbox(
            "Multiple lines",
            ["No", "Yes"]
        )

internet_service = st.selectbox(
    "Internet service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online security",
    ["No internet service"] if internet_service == "No" else ["No", "Yes"],
    disabled=(internet_service == "No")
)

online_backup = st.selectbox(
    "Online backup",
    ["No internet service"] if internet_service == "No" else ["No", "Yes"],
    disabled=(internet_service == "No")
)

device_protection = st.selectbox(
    "Device protection",
    ["No internet service"] if internet_service == "No" else ["No", "Yes"],
    disabled=(internet_service == "No")
)

tech_support = st.selectbox(
    "Tech support",
    ["No internet service"] if internet_service == "No" else ["No", "Yes"],
    disabled=(internet_service == "No")
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["No internet service"] if internet_service == "No" else ["No", "Yes"],
    disabled=(internet_service == "No")
)

streaming_movies = st.selectbox(
    "Streaming movies",
    ["No internet service"] if internet_service == "No" else ["No", "Yes"],
    disabled=(internet_service == "No")
)



# Ensure service selections are consistent
if phone_service == "No":
    multiple_lines = "No phone service"

if internet_service == "No":
    online_security = "No internet service"
    online_backup = "No internet service"
    device_protection = "No internet service"
    tech_support = "No internet service"
    streaming_tv = "No internet service"
    streaming_movies = "No internet service"
else:
    # Internet customers cannot have "No internet service"
    # as the value for an individual internet feature.
    online_security = (
        "No" if online_security == "No internet service"
        else online_security
    )
    online_backup = (
        "No" if online_backup == "No internet service"
        else online_backup
    )
    device_protection = (
        "No" if device_protection == "No internet service"
        else device_protection
    )
    tech_support = (
        "No" if tech_support == "No internet service"
        else tech_support
    )
    streaming_tv = (
        "No" if streaming_tv == "No internet service"
        else streaming_tv
    )
    streaming_movies = (
        "No" if streaming_movies == "No internet service"
        else streaming_movies
    )

# Build a single customer record
customer_data = pd.DataFrame([{
    "gender": gender,
    "SeniorCitizen": 1 if senior_citizen == "Yes" else 0,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone_service,
    "MultipleLines": multiple_lines,
    "InternetService": internet_service,
    "OnlineSecurity": online_security,
    "OnlineBackup": online_backup,
    "DeviceProtection": device_protection,
    "TechSupport": tech_support,
    "StreamingTV": streaming_tv,
    "StreamingMovies": streaming_movies,
    "Contract": contract,
    "PaperlessBilling": paperless_billing,
    "PaymentMethod": payment_method,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges
}])



st.divider()

st.subheader("Customer Churn Risk Assessment")

if st.button("Predict Churn Risk", type="primary"):

    # Generate the customer's predicted churn probability
    churn_probability = model.predict_proba(
        customer_data
    )[0, 1]

    # Use our cross-validated decision threshold
    threshold = 0.30

    st.markdown("### Prediction Results")

    st.metric(
        label="Predicted Churn Probability",
        value=f"{churn_probability:.1%}"
    )

    st.progress(float(churn_probability))
    st.caption("The bar represents the model's estimated churn probability.")

    if churn_probability >= threshold:
        st.warning(
            "Elevated predicted churn risk. "
            "This customer may warrant retention review."
        )

        st.info(
            "Suggested action: Consider reviewing this customer's "
            "service experience and whether a suitable retention "
            "offer or support intervention is appropriate."
        )
    else:
        st.success(
            "Lower predicted churn risk based on "
            "the selected model threshold."
        )

    st.caption(
        "Predictions are based on historical customer data. "
        "They are estimates, not guarantees of future behaviour."
    )



st.divider()
st.caption(
    "Model: Logistic Regression | "
    "Decision threshold: 30% | "
    "Dataset: IBM Telco Customer Churn"
)
