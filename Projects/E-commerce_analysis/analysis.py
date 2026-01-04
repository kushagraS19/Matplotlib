import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "D:/Kushagra/Data-science/Matplotlib/Projects/E-commerce_analysis/data.csv",
    encoding="ISO-8859-1"
)
print(df.head())

df = df.dropna(subset=["CustomerID"])
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
df = df[(df["Quantity"] > 0) & df["UnitPrice"] > 0]

# Total price --> 

df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
print(df.head())

# String to dateTime object
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# customer level aggregation

snapshot_date = df["InvoiceDate"].max()

customer_df = df.groupby("CustomerID").agg(
    Recency = ("InvoiceDate","max"),
    Frequency = ("InvoiceNo","nunique"),
    Monetary = ("TotalPrice","sum")
)

customer_df["Recency"] = (snapshot_date - customer_df["Recency"]).dt.days
customer_df.columns = ["Recency" , "Frequency" , "Monetary"]

customer_df["R"] = pd.qcut(customer_df["Recency"],4, labels = [4,3,2,1])
customer_df["F"] = pd.qcut(customer_df["Frequency"].rank(method = "first"),4 , labels = [1,2,3,4])
customer_df["M"] = pd.qcut(customer_df["Monetary"],4, labels = [1,2,3,4])

customer_df["RFM_Score"] = (
    customer_df["R"].astype(str) +
    customer_df["F"].astype(str) + 
    customer_df["M"].astype(str)
)
print()
print(customer_df)

# Top 10 customers --> 

top_customers = customer_df.sort_values(
    "Monetary", ascending = False
).head(10)
print()
print(top_customers)

# Spending distribution histogram --> 

plt.hist(customer_df["Monetary"], bins = 20)
plt.title("Customer spending distribution")
plt.xlabel("Total spend")
plt.ylabel("No. of customers")
plt.tight_layout()
plt.savefig("Customer_spending.png", dpi = 300, bbox_inches = "tight")
plt.show()

# Purchase frequency VS spending

plt.scatter(customer_df["Frequency"], customer_df["Monetary"])
plt.title("Purchase frequency VS spending")
plt.xlabel("Frequnecy")
plt.ylabel("Monetary value")
plt.tight_layout()
plt.savefig("Frequency_VS_spending.png", dpi = 300, bbox_inches = "tight")
plt.show()