import matplotlib.pyplot as plt 

region = ["North","South",'East','West']
revenue = [100000,200000,150000,45000]

plt.pie(revenue , labels = region , autopct="%1.1f%%", colors=["gold",'skyblue','burlywood','hotpink'])
plt.show()