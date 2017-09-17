import matplotlib.pyplot as plt

x_values = list(range(1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,
            y_values,
            edgecolor='none',
            c=y_values,
            s=10,
            cmap=plt.cm.Blues)

#plt.axis([0, 1100, 0, 1100000])

plt.show()
