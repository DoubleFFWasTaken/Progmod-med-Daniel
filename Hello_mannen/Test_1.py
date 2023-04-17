import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,6,8,10,12,14,16,18,20]

x1 = [1,2,3,4,5,6,7,8,9,10]
y1 = [0,0,0,0,0,-1,-2,-3,-4,-5]

x2 = []
y2 = []


def f(x):
    y = -(x**2)
    return y

x = 1
while x <= 10:
    y2.append(f(x))
    x2.append(x)
    x += 1
    
plt.plot(x,y,label="gaming hours")
plt.plot(x1,y1,label="women talked to")
plt.plot(x2,y2, label="will to live")
plt.legend()
plt.grid()
plt.show()
