
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_excel("sellers.xlsx")

# Title
st.title("Sellers Dashboard")

# Sidebar: Filter by Region
st.sidebar.header("Filter Options")
regions = df["REGION"].unique()
selected_region = st.sidebar.selectbox("Select Region", options=regions)

# Filtered DataFrame
filtered_df = df[df["REGION"] == selected_region]

# Container to display the table
with st.container():
    st.subheader(f"Seller Data - Region: {selected_region}")
    st.dataframe(filtered_df)

# Graphs
with st.container():
    st.subheader("Sales Visualizations")

    col1, col2 = st.columns(2)

    # Units Sold per Region
    with col1:
        units_sold = df.groupby("REGION")["UNIDADES VENDIDAS"].sum()
        st.write("Total Units Sold by Region")
        fig1, ax1 = plt.subplots()
        units_sold.plot(kind="bar", ax=ax1)
        ax1.set_ylabel("Units Sold")
        st.pyplot(fig1)

    # Total Sales per Region
    with col2:
        total_sales = df.groupby("REGION")["VENTAS TOTALES"].sum()
        st.write("Total Sales by Region")
        fig2, ax2 = plt.subplots()
        total_sales.plot(kind="bar", ax=ax2, color="green")
        ax2.set_ylabel("Total Sales")
        st.pyplot(fig2)

    # Average Sales per Vendor per Region
    avg_sales = df.groupby("REGION")["VENTAS TOTALES"].mean()
    st.write("Average Sales per Vendor by Region")
    fig3, ax3 = plt.subplots()
    avg_sales.plot(kind="bar", ax=ax3, color="orange")
    ax3.set_ylabel("Average Sales")
    st.pyplot(fig3)

# Specific Vendor Lookup
with st.container():
    st.subheader("Vendor Lookup")
    vendor_id = st.text_input("Enter Vendor ID or Name (partial allowed):")

    if vendor_id:
        filtered_vendor = df[
            df["ID"].astype(str).str.contains(vendor_id, case=False) |
            df["NOMBRE"].str.contains(vendor_id, case=False) |
            df["APELLIDO"].str.contains(vendor_id, case=False)
        ]
        if not filtered_vendor.empty:
            st.dataframe(filtered_vendor)
        else:
            st.warning("No vendor found with that input.")
