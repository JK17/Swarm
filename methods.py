import numpy as np

def get_positions(swarm, N):
    positions = np.empty((N,2))

    for i in range(N):
        positions[i][0] = swarm.X[i]
        positions[i][1] = swarm.Y[i]
    
    return positions

def change_dist(dist):
    dist[dist != 0] = 1

    return dist

def average_velocity(dist, swarm, N):
    av_vel = np.dot(dist, swarm.direction)
    av_vel = np.reshape(av_vel, (N,1))

    return av_vel
        
def adjust_angle(swarm, av_vel, a):
    for i, theta_i in enumerate(swarm.theta):
        swarm.theta[i] =  np.angle(av_vel[i]) + a * np.random.uniform(-np.pi, np.pi)
        

