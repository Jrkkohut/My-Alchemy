import numpy as np
import random

d0 = np.array(42)
d1 = np.array((42, 42, 42))
d2 = np.array([[1, 2, 3], [4, 5, 6]])
d3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

dn = np.array([1,2,3], ndmin=5)

nplist = np.array([random.randint(1, 1000) for i in range(100)])
#nplist3d = nplist.reshape(4, 5, 5)

filter = []
for i in range(100):
	filter.append(i % 2 == 0)
x = np.random.randint(0, 100, size=(4, 4, 10))


x = np.random.choice([1, 2, 3, 4], p=[0.1, 0.3, 0.4, 0.2], size=(100))
# print(len(np.where(x == 1)[0]))
# print(len(np.where(x == 2)[0]))
# print(len(np.where(x == 3)[0]))
# print(len(np.where(x == 4)[0]))
import matplotlib.pyplot as plt
import seaborn as sb
x = np.random.exponential(scale=8, size=10000)
y = np.random.poisson(lam=8, size=10000)
z = np.random.zipf(a=1.1, size=10000)
#sb.distplot(x, hist=True, kde=True, label="exponential")
#sb.distplot(y, hist=True, kde=True, label="poisson")
sb.distplot(z[z<5], kde=True, hist=False, label="zipf")
plt.legend()
plt.show()

