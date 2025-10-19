import streamlit as st
import pandas as pd
from datetime import date

st.title("🧠 Coding Timer Tracker")

# Input waktu coding
hours = st.number_input("Berapa jam kamu coding hari ini?", min_value=0.0, max_value=24.0, step=0.5)
submit = st.button("Simpan")

# Simpan ke CSV
if submit and hours > 0:
    data = pd.DataFrame([[str(date.today()), hours]], columns=["Tanggal", "Jam"])
    try:
        old = pd.read_csv("coding_log.csv")
        data = pd.concat([old, data], ignore_index=True)
    except FileNotFoundError:
        pass
    data.to_csv("coding_log.csv", index=False)
    st.success("Data disimpan!")

# Tampilkan statistik
try:
    df = pd.read_csv("coding_log.csv")
    total = df["Jam"].sum()
    st.subheader(f"Total waktu coding: {total:.1f} jam")
    st.line_chart(df.set_index("Tanggal"))
except FileNotFoundError:
    st.info("Belum ada data tersimpan.")
