import matplotlib
matplotlib.use('Qt5Agg') # Switches to a separate interactive GUI window
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6])
plt.axis('tight')
plt.show()