import streamlit as st
import pandas as pd
import time

st.title("💳 Real-Time Fraud Detection System")

placeholder = st.empty()

while True:
    try:
        df = pd.read_csv(
            "fraud_results.csv",
            names=["user_id","amount","location","timestamp","status","risk_score","reason"]
        )

        fraud_count = len(df[df["status"] == "FRAUD"])

        placeholder.container()
        st.metric("Total Transactions", len(df))
        st.metric("Fraud Cases", fraud_count)

        st.dataframe(df.tail(10))

    except:
        st.write("Waiting for data...")

    time.sleep(2)