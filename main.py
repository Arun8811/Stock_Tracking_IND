import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.set_page_config(layout="wide")

st.title("📊 Stock Tracking IND")
st.subheader("A platform to share knowledge and grow together as a community :)")
st.divider()
st.badge("Disclaimer: Invest after consulting with a SEBI registered financial advisor.", color='red')

#Google Sheet URL
url = "https://docs.google.com/spreadsheets/d/1MK8GYDKYCrAnClUSMuolPxiju07TSDLnOvVtJIbcXbE/edit?gid=979918604#gid=979918604"

#Read directly into a DataFrame
df = pd.DataFrame({
  'Stock Name': ["Aditya Birla Capital", "CIPLA", "DRREDDY", "ITC",],
  'Symbol': ["ABCAPITAL", "CIPLA", "DRREDDY", "ITC"],
  'CMP': [140, 1100, 1500, 200],
  'Buy Price': [152, 1200, 1300, 500], 
})


# Add recommendation column
data["Recommendation"] = data.apply(
    lambda row: "Consider" if row["CMP"] < row["Buy Price"] else "Diamond Needle",
    axis=1
)

# Function to color the Decision column
def color_decision(row):
    if row["Recommendation"] == "Consider":
        return ["background-color: #d4edda; color: green; font-weight: bold"]*len(row)
    else:
        return ["background-color: #f8d7da"]*len(row)


# Apply styling
styled_df = data.style.apply(color_decision, axis=1)

st.dataframe(styled_df, use_container_width=True)
