import matplotlib.pyplot as plt

months = [1,2,3,4]
sales = [100,200,150,345]

# plt.plot (data on x - axis , data on y -  axis)
# color --> Color of line
# linestyle --> Style of line
# linewidth --> thickness of line
# marker --> Marks the data points
# label --> What is the data about
plt.plot(months, sales, color="pink", linestyle = "--",linewidth = 2.5,marker = "o", label = "2025 Sales") # Creates a line graph.

plt.show()