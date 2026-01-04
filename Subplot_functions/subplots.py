import matplotlib.pyplot as plt

# plt.subplot(no. of rows, no. of columns, index)

x = [1,2,3,4]
y = [10,20,35,46]

plt.subplot(1,2,1) # 1st row, 2nd column, 1st subplot
plt.plot(x,y)
plt.title("Line chart")

plt.subplot(1,2,2)
plt.bar(x,y)
plt.title("Bar chart")

plt.show()