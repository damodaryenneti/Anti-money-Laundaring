import streamlit as st
import pandas as pd
import joblib
from keras.models import load_model

st.set_page_config(page_title='AML Detection System', page_icon='🏦', layout='centered')

# ---------- Background and styling ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    background-attachment: fixed;
}
[data-testid="stHeader"] {background: transparent;}
.block-container {
    background: rgba(255, 255, 255, 0.07);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 16px;
    padding: 2rem 2.5rem;
    margin-top: 2rem;
    backdrop-filter: blur(8px);
}
h1, h2, h3, p, [data-testid="stWidgetLabel"] p {color: #ffffff !important;}
div.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.6rem;
    font-weight: 600;
}
div.stButton > button:hover {opacity: 0.9; color: white;}
</style>
""", unsafe_allow_html=True)

# ---------- Load model and preprocessor once ----------
@st.cache_resource
def load_artifacts():
    model = load_model('AML.keras')
    preprocessor = joblib.load('preprocessor')
    return model, preprocessor

model, preprocessor = load_artifacts()

# ---------- UI ----------
st.title('🏦 Anti Money Laundering System')
st.write('Enter the transaction details to check whether it looks suspicious.')

currencies = ['UK pounds', 'Dirham', 'Albanian lek', 'Euro', 'Swiss franc',
              'Moroccan dirham', 'Mexican Peso', 'Indian rupee', 'Naira',
              'Turkish lira', 'Pakistani rupee', 'US dollar', 'Yen']

locations = ['UK', 'Albania', 'Netherlands', 'Morocco', 'Germany', 'Mexico',
             'Switzerland', 'Spain', 'Italy', 'India', 'Nigeria', 'France',
             'UAE', 'Turkey', 'Japan', 'Pakistan', 'USA', 'Austria']

payment_types = ['Cash Withdrawal', 'ACH', 'Cash Deposit', 'Cheque',
                 'Debit card', 'Cross-border', 'Credit card']

amount = st.number_input('Amount', min_value=0.01, value=1000.0, step=100.0)

col1, col2 = st.columns(2)
with col1:
    payment_currency = st.selectbox('Payment currency', currencies)
    sender_location = st.selectbox('Sender bank location', locations)
with col2:
    received_currency = st.selectbox('Received currency', currencies)
    receiver_location = st.selectbox('Receiver bank location', locations)

payment_type = st.selectbox('Payment type', payment_types)

# Column names MUST match the training data exactly
input_data = pd.DataFrame({
    'Amount': [amount],
    'Payment_currency': [payment_currency],
    'Received_currency': [received_currency],
    'Sender_bank_location': [sender_location],
    'Receiver_bank_location': [receiver_location],
    'Payment_type': [payment_type]
})

THRESHOLD = 0.5   # replace with the best threshold found on your test set

if st.button('Predict'):
    X_new = preprocessor.transform(input_data)
    if hasattr(X_new, 'toarray'):      # OneHotEncoder may return a sparse matrix
        X_new = X_new.toarray()

    prob = float(model.predict(X_new, verbose=0)[0][0])

    st.progress(min(max(prob, 0.0), 1.0))
    st.write(f'Suspicion score: **{prob:.2%}**')

    if prob >= THRESHOLD:
        st.error('⚠️ Suspicious transaction: possible Money Laundering')
    else:
        st.success('✅ Legitimate transaction')