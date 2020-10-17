# dynamic.py


import matplotlib.pyplot as plt 


px0, py0 = list(map(int,input('Input initial position: ').split()))
vx0, vy0 = list(map(int,input('Input initial velocity: ').split()))
g = 10
px, py = [],[]

for t in range(50):
    px.append(px0 + vx0 * (t * 0.1))
    py.append(py0 + vy0 * (0.1*t) - 0.5 * g * (0.1*t)**2)

plt.scatter(px,py)
plt.show()

