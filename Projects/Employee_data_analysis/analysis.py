import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = "Employee_updated.csv"

df = pd.read_csv(data)
df = df[df['Salary'] > 0]

mean = np.mean(df["Salary"])
median = np.median(df["Salary"])
std_dev = np.std(df["Salary"])
summary = {
    "Mean" : mean,
    "Median" : median,
    "Standard Deviation" : std_dev,
}
print(summary)

# Minimum , maximum , mean salary of each department -->

dept_salary = df.groupby("Team")['Salary'].agg(["mean", "min", "max"])
print(dept_salary)

# Bar graph showing average salary by department --> 

plt.figure(figsize=(8,6))
dept_salary['mean'].plot(kind="bar")
plt.title("Average salary by department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.tight_layout()
plt.savefig("Average_salary.png",dpi = 300, bbox_inches = "tight")
plt.show()

# Gender pay gap -->

gender_salary = df.groupby('Gender')['Salary'].mean()
pay_gap = gender_salary.max() - gender_salary.min()
print("Gender Pay Gap :",pay_gap) 

# Salary Outlier detection --> 

Q1 = np.percentile(df["Salary"],25)
Q2 = np.percentile(df["Salary"],75)
IQR = Q2 - Q1

outliers = df[
    (df["Salary"] < Q1 - 1.5 * IQR) | (df["Salary"] > Q2 + 1.5 * IQR)
]
print("Outliers :\n", outliers)

# Salary box plot --> 

plt.boxplot(df["Salary"])
plt.title("Salary distrubution & outliers")
plt.ylabel("Salary -->")
plt.tight_layout()
plt.savefig("Salary_distribution.png", dpi = 300, bbox_inches = "tight")
plt.show()