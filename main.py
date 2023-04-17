import numpy as np

G = 6.67*10**-11

def getAcceleration(pos, mass, softening):
    N = pos.shape[0]
    a = np.zeros((N,3))

    for i in range(N):
        for j in range(N):
            dx = pos[i,0] - pos[j, 0]
            dy = pos[i,1] - pos[j, 0]
            dz = pos[i,2] - pos[j, 0]
            inverseSquare = (dx**2 + dy**2 + dz**2 + softening**2)**(-1.5)
            a[j, 0] += inverseSquare * mass[i] * dx * G
            a[j, 1] += inverseSquare * mass[i] * dy * G
            a[j, 2] += inverseSquare * mass[i] * dz * G

    return a
