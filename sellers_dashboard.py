
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_excel("sellers.xlsx")

# Title
st.title("Sellers Dashboard")

# Sidebar filter for region
st.sidebar.header("Filter Options")
selected_region = st.sidebar.selectbox("Select Region", options=df['REGION'].unique())
filtered_df = df[df['REGION'] == selected_region]

# Display filtered data
st.subheader(f"Vendor Data - Region: {selected_region}")
st.dataframe(filtered_df)

# Summary stats
with st.container():
    st.subheader("Sales Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Units Sold", int(filtered_df['UNIDADES VENDIDAS'].sum()))
    col2.metric("Total Sales", f"${int(filtered_df['VENTAS TOTALES'].sum()):,}")
    col3.metric("Average Sales", f"${int(filtered_df['VENTAS TOTALES'].mean()):,}")

# Graphs section
st.subheader("Sales Graphs")

# Units Sold Bar Chart
fig1, ax1 = plt.subplots()
ax1.bar(filtered_df['NOMBRE'] + " " + filtered_df['APELLIDO'], filtered_df['UNIDADES VENDIDAS'])
plt.xticks(rotation=90)
ax1.set_title("Units Sold per Vendor")
ax1.set_ylabel("Units Sold")
st.pyplot(fig1)

# Total Sales Bar Chart
fig2, ax2 = plt.subplots()
ax2.bar(filtered_df['NOMBRE'] + " " + filtered_df['APELLIDO'], filtered_df['VENTAS TOTALES'])
plt.xticks(rotation=90)
ax2.set_title("Total Sales per Vendor")
ax2.set_ylabel("Sales ($)")
st.pyplot(fig2)

# Average Sales Pie Chart
avg_sales = filtered_df[['NOMBRE', 'APELLIDO', 'VENTAS TOTALES']].copy()
avg_sales['Full Name'] = avg_sales['NOMBRE'] + " " + avg_sales['APELLIDO']
fig3, ax3 = plt.subplots()
ax3.pie(avg_sales['VENTAS TOTALES'], labels=avg_sales['Full Name'], autopct='%1.1f%%')
ax3.set_title("Sales Distribution")
st.pyplot(fig3)

# Vendor-specific display
st.subheader("Vendor Lookup")
vendor_list = df['NOMBRE'] + " " + df['APELLIDO']
selected_vendor = st.selectbox("Select a Vendor", vendor_list)

vendor_info = df[vendor_list == selected_vendor]
if not vendor_info.empty:
    st.write("### Vendor Information")
    st.write(vendor_info)
