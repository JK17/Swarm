import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree
import methods as m
from classes import Swarm
from initial import L, N, r, r_b, v_0, a

swarm = Swarm(N, L)

plt.quiver(swarm.X, swarm.Y, swarm.U, swarm.V, swarm.theta)
plt.show()

positions = m.get_positions(swarm, N)
birds_tree = cKDTree(positions,boxsize=[L,L])
dist = birds_tree.sparse_distance_matrix(birds_tree,max_distance=r,output_type='coo_matrix')
dist = dist.todense()

m.change_dist(dist)

av_vel = m.average_velocity(dist, swarm, N)

m.adjust_angle(swarm, av_vel, a)
