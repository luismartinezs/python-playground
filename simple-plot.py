import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, marker = 'o')
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Simple plot')
plt.show()