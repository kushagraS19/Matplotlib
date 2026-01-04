import matplotlib.pyplot as plt

# savefig("Filename.extension", dpi = value , bbox_inches = "tight")
# dpi (dots per inch) --> Controls image resolution
# bbox_inches = controls white spaces around the graph.

x = [1,2,3,4]
y = [10,20,15,25]

plt.plot(x,y,color = "blue", marker = "o")
plt.title("Line chart")
plt.savefig("Line.png", dpi = 300 , bbox_inches = "tight") 