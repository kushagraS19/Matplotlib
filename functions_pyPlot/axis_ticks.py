import matplotlib.pyplot as plt

months = [1,2,3,4]
sales = [100,200,150,345]

plt.plot(months, sales, color="pink", linestyle = "--",linewidth = 2.5,marker = "o", label = "2025 Sales") # Creates a line graph.
plt.xlabel("Months --> ")
plt.ylabel("Sales on that month --> ")

plt.title("2025 Monthly sales")

plt.xticks([1,2,3,4], ['M1','M2','M3','M4'])
plt.yticks([100,200,150,345],['s1','s2','s3','s4'])

plt.show()