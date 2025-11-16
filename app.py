# Write the Streamlit app to a file

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("pakwheels_listings.csv")

# Preprocess numeric columns
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["engine_cc"] = df["engine"].str.extract(r"(\d+)").astype(float)
df["mileage_km"] = df["mileage"].str.replace(",", "", regex=True).str.extract(r"(\d+)").astype(float)
df["year"] = pd.to_numeric(df["model_year"], errors="coerce")
df["city"] = df["description"].str.extract(r"in\s+([A-Za-z ]+)$")

st.title("PakWheels Used Cars Analysis")

# Price Distribution
st.subheader("Price Distribution")
fig, ax = plt.subplots()
df["price"].dropna().plot.hist(bins=20, ax=ax)
ax.set_xlabel("Price")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Engine Size Distribution
st.subheader("Engine Size Distribution (CC)")
fig, ax = plt.subplots()
df["engine_cc"].dropna().plot.hist(bins=20, ax=ax)
ax.set_xlabel("Engine CC")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Mileage Distribution
st.subheader("Mileage Distribution (KM)")
fig, ax = plt.subplots()
df["mileage_km"].dropna().plot.hist(bins=20, ax=ax)
ax.set_xlabel("Mileage KM")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# City-wise Concentration
st.subheader("Cars per City")
fig, ax = plt.subplots()
df["city"].value_counts().plot.bar(ax=ax)
ax.set_xlabel("City")
ax.set_ylabel("Count")
st.pyplot(fig)

# Brand-Year Aging Pattern
st.subheader("Brand-Year Count")
fig, ax = plt.subplots()
df.groupby(["brand", "year"]).size().plot.bar(ax=ax)
ax.set_xlabel("Brand, Year")
ax.set_ylabel("Count")
st.pyplot(fig)

# Best Car Selection
st.subheader("Best Car Available")
df_sorted = df.sort_values(by=["year", "mileage_km", "price"], ascending=[False, True, True])
best_car = df_sorted.iloc[0]
st.write(best_car)
