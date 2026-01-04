import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Employee_updated.csv")
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

dept_salary = df.groupby("Team")['Salary'].agg(["mean", "min", "max"])
print(dept_salary)

plt.figure(figsize=(8,6))
dept_salary['mean'].plot(kind="bar")
plt.title("Average salary by department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.tight_layout()
plt.savefig("Average_salary.png",dpi = 300, bbox_inches = "tight")
plt.show()

gender_salary = df.groupby('Gender')['Salary'].agg(["mean", "max", "min"])
print(gender_salary)

