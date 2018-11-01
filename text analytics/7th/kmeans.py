#Taken from https://datasciencelab.wordpress.com/2013/12/12/clustering-with-k-means-in-python/
# Just added plotting for 3-k cases

import numpy as np
import random
import matplotlib.pyplot as plt

def init_board(N):
    return np.array([(random.uniform(-15,15),random.uniform(-15,15)) for i in range(N)])
    #X = np.array([(random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(N)])
    #return X

def cluster_points(X, mu):
    clusters  = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
                    for i in enumerate(mu)], key=lambda t:t[1])[0]
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters

def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(clusters[k], axis = 0))
    return newmu

def has_converged(mu, oldmu):
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))

def find_centers(X, K):
    # Initialize to K random centers
    oldmu = random.sample(X, K)
    mu = random.sample(X, K)
    while not has_converged(mu, oldmu):
        oldmu = mu
        # Assign all points in X to clusters
        clusters = cluster_points(X, mu)
        # Reevaluate centers
        mu = reevaluate_centers(oldmu, clusters)
    return(mu, clusters)

def change_coords(array):
    return list(map(list, zip(*array)))

def parse_output(data):
    clusters = data[1]
    points1 = change_coords(clusters[0])
    plt.plot(points1[0], points1[1], 'ro')
    points2 = change_coords(clusters[1])
    plt.plot(points2[0], points2[1], 'g^')
    points3 = change_coords(clusters[2])
    plt.plot(points3[0], points3[1], 'ys')
    centroids = change_coords(data[0])
    plt.plot(centroids[0], centroids[1], 'kx')
    plt.axis([-15, 15, -15, 15])
    plt.show()

#data = init_board(15)
for i in range(20):
    data = np.array([[  2.12 ,3.4],
 [3 , 3.7],
 [  2.5,  4.5],
 [  1.1 , 2.9],
 [ 1.8 , 4.1],
 [ -13.6 , -10.7 ],
 [  -13.7 ,-10],
 [  -13.65  ,-10.9],
 [  -14.1  ,-10.6],
 [ -12.9  ,-11.21],
 [7.5  ,-10.8],
 [ 7.77  ,-11.6],
 [ 7.80 , -9.6],
 [ 7.1  , -11.2],
 [  8.90  , -8.98]])
    #print(data)
    ##print(type(data))
    out=key,value = find_centers(list(data), 3)
    print("iteration",i,"=",key[0],key[1],key[2])
    #parse_output(out)
