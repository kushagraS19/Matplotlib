import matplotlib.pyplot as plt

# We can set figure size and axis
# fig, ax = plt.subplots(no. of rows, no. of columns, figsize = (width , height))
fig , ax = plt.subplots(1,2,figsize = (10,6))

x = [1,2,3,4]
y = [10,20,15,46]

ax[0].plot(x,y)
ax[0].set_title("Line graph")

ax[1].bar(x,y)
ax[1].set_title("Bar graph")

plt.tight_layout()
plt.show()