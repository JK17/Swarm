import numpy as np

class Swarm:
    def __init__(self, N, L):
        self.X = np.empty(N)
        self.Y = np.empty(N)
        self.theta = np.empty(N)
        self.direction = np.empty(N, dtype=np.complex128)
        self.U = np.empty(N)
        self.V = np.empty(N)  
        for i in range(N):
            self.X[i] = np.random.uniform(0,L)
            self.Y[i] = np.random.uniform(0,L)
            self.theta[i] = np.random.uniform(-np.pi, np.pi)
            self.direction[i] = np.exp( (0+1j) * self.theta[i])
            self.U[i] = np.cos(self.theta[i])
            self.V[i] = np.sin(self.theta[i])