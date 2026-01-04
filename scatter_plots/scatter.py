import matplotlib.pyplot as plt

# One Group -->>>>

# hours = [1,2,3,4,5,6,7,8]
# score = [50,55,60,65,70,75,80,85]

# plt.scatter(hours, score , color="magenta",marker='v')
# plt.grid(color = "grey")
# plt.show()

#_____________________________________________________________________________________________________

# Two Group -->>>>>>

plt.scatter([1,2,3],[45,50,60],color = "blue", label = "Class A")
plt.scatter([1,2,3],[40,45,65],color = "hotpink", label = "Class B")

plt.grid(color = "grey")
plt.legend()
plt.show()