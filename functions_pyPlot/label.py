import matplotlib.pyplot as plt

months = [1,2,3,4]
sales = [100,200,150,345]

plt.plot(months, sales, color="pink", linestyle = "--",linewidth = 2.5,marker = "o", label = "2025 Sales") # Creates a line graph.
plt.xlabel("Months --> ")
plt.ylabel("Sales on that month --> ")

plt.show()