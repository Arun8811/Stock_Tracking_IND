import streamlit as st
import pandas as pd

st.title("📊 Stock Tracking IND")

# Extract your unique Sheet ID from your browser's address bar
# sheet_id = "1MK8GYDKYCrAnClUSMuolPxiju07TSDLnOvVtJIbcXbE"

# Construct the direct export URL
# url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

#Read directly into a DataFrame
df = pd.DataFrame({
  'Stock Name': ["Aditya Birla Capital", "CIPLA", "DRREDDY", "ITC",],
  'Symbol': ["ABCAPITAL", "CIPLA", "DRREDDY", "ITC"],
  'CMP': [140, 1100, 1500, 200],
  'Buy Price': [152, 1200, 1300, 500], 
})


# Add recommendation column
df["Recommendation"] = df.apply(
    lambda row: "Consider" if row["CMP"] < row["Buy Price"] else "Diamond Needle",
    axis=1
)

# Function to color the Decision column
def color_decision(val):
    if val == "Consider":
        return "background-color: #d4edda; color: green; font-weight: bold"
    else:
        return "background-color: #f8d7da; color: red; font-weight: bold"


# Apply styling
styled_df = df.style.map(color_decision, subset=["Recommendation"])

st.dataframe(styled_df, use_container_width=True)