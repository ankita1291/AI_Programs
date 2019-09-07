
from math import sqrt
import random
import matplotlib.pyplot as plt

class Kmeans(object):
    def __init__(self, data, k=4):
        def kcluster(data, k=4):
            
            ranges = [ (min([ d[i] for d in data ]), \
                            max([ d[i] for d in data])) for i in range(len(data[0])) ]
            # k random centroids
           
            centroids = [ [ random.random()*(ranges[i][1] - ranges[i][0])+ranges[i][0] \
                           for i in range(len(data[0])) ] for j in range(k) ]

            lastmatches = None
            bestmatches = None
            t = 0

            for t in range(100):
                print ('Iteration %d' % t)
                bestmatches = [ [] for i in range(k) ]

                # Find which centroid(centroids[i]) is the closest for each data
                for j in range(len(data)):
                    dj = data[j]
                    bestmatch = 0
                    for i in range(k):
                        d = self.distance(centroids[i], dj)
                        if d < self.distance(centroids[bestmatch], dj):
                            # closest cluster number
                            bestmatch = i
                    # append index j to i(bestmatch) th cluster
                    bestmatches[bestmatch].append(j)

                # if the results are the same as last time, this is complete
                if bestmatches == lastmatches: break
                lastmatches = bestmatches
                
                # move the centroids(centroids[i]) to the mean of their members
                for i in range(k):
                    mean = [0.0] * len(data[0])
                    if len(bestmatches[i]) > 0:
                        for data_id in bestmatches[i]:
                            for dim in range(len(data[data_id])):
                                mean[dim] += data[data_id][dim]
                        for j in range(len(mean)):
                            mean[j] /= len(bestmatches[i])
                        centroids[i] = mean

            return bestmatches, centroids

        self.clusters, self.centers = kcluster(data, k)
            
    @staticmethod
    def clustering(data, k=4):
        sets = Kmeans(data, k)
        return sets
    
    def pearson(self, v1, v2):
        n = len(v1)
        
        sum1 = sum(v1)
        sum2 = sum(v2)

        sum1Sq = sum([ pow(v, 2) for v in v1 ])
        sum2Sq = sum([ pow(v, 2) for v in v2 ])

        pSum = sum([ v1[i] * v2[i] for i in range(len(v1)) ])

        # pearson score
        num = pSum - (sum1 * sum2 / len(v1))
        den = sqrt( (sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n) )
        if den == 0: return 0

        # high correlation -> small distance 
        return 1.0 - num/den

    def distance(self, v1, v2):
        d = 0.0
        for i in range(len(v1)):
            d += (v1[i] - v2[i])**2
        return sqrt(d)

def main():
    # test data
    # 2-d vector
    data = np.loadtxt('GMM_dataset.txt')
    # kmeans clustering
    km_sets = Kmeans.clustering(data, 3)

    # plot result
    plt.grid(True)
    color = [ ['bo', 'b'], ['go', 'g'], ['ro', 'r'], \
                  ['co', 'c'], ['mo', 'm'], ['yo', 'y'], ['ko', 'k'], ['wo', 'w'] ] # 8クラスタまで色分け可
    for i in range(len(km_sets.clusters)):
        print( "class #%d: %d pts." %(i, len(km_sets.clusters[i])))
        if len(km_sets.clusters[i]) > 0:
            color_idx = i % len(color)
            
          
            xc = km_sets.centers[i][0]
            yc = km_sets.centers[i][1]
            plt.plot(xc, yc, color[color_idx][0], ms=9.0, zorder=3)

           
            for j in range(len(km_sets.clusters[i])):
                x = data[ km_sets.clusters[i][j] ][0]
                y = data[ km_sets.clusters[i][j] ][1]
                plt.plot([x, xc], [y, yc], color[color_idx][1], zorder=1)
                plt.plot(x, y, color[color_idx][0], zorder=2)
    plt.show()

if __name__ == '__main__':
    main()