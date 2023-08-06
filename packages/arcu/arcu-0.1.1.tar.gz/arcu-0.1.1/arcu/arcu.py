import time
import numpy as np
import pandas as pd

# A is a pandas dataframe, with columns: index, x-coord, y-coord, feat1 ... feat
# r is a radius parameter, which determines the pixel radius you're going to consider each spatial group
# c is a minimum cell count parameter, which determines the minimum cell count for a group to be reported 
# u is a scale-threshold parameter, which determines the coefficient on standard deviation for thresholding cells
# --> returns a dataframe of x,y coordinates within a population of cells where you can find representative subpopulations

def arcu(A, r, c, u):
    startall = time.time()
    print('Deframing data...')
    arr = A.to_numpy()
    feats = arr.shape[1] - 3
    cells = arr.shape[0]
    print('Data loaded. Found', feats, 'features across', cells, 'cells.')
    print('Initializing quality control...')
    start = time.time()
    B = step0_IQC(arr)
    end = time.time()
    print('Finished quality control. Elapsed', (end - start)/60, 'minutes.')
    print('Building candidate neighborhoods...')
    start = time.time()
    G, L = step1_BCN(B, r, c)
    end = time.time()
    CNs = L.shape[0]
    print('Found', CNs, 'candidate neighborhoods. Elapsed', (end - start)/60, 'minutes.')
    print('Evaluating candidate neighborhoods...')
    start = time.time()
    E = step2_ECN(B, G, u)
    end = time.time()
    PNs = E.shape[0]
    print(PNs, 'neighborhoods were classified. Elapsed', (end - start)/60, 'minutes.')
    print('Identifying centroids for passed neighborhoods...')
    start = time.time()
    XY = step3_EXY(L, E, G) 
    end = time.time()
    ACs = XY.shape[0]
    print(ACs, 'neighborhoods passed across', PNs, 'candidate neighborhoods. Elapsed', (end - start)/60, 'minutes.')
    print('Recording centroids and reframing data...')
    df = pd.DataFrame(XY, columns = ['X','Y'])
    endall = time.time()
    print('Done! Total time computing:', (endall - startall)/60, 'minutes.')
    return df

def step0_IQC(arr): # in development
    B = arr
    return B

def step1_BCN(B, r, c): 
    R = np.zeros((np.size(B,0),np.size(B,0)))
    for i in np.arange(np.size(B,0)):
        for j in np.arange(np.size(B,0)):
            R[i,j] = np.sqrt((B[i,1] - B[j,1])**2 + (B[i,2] - B[j,2])**2)
    N = np.zeros((np.size(R,0),np.size(R,0)))
    for i in np.arange(np.size(R,0)):
        for j in np.arange(np.size(R,0)):
            if (R[i,j] < r):
                N[i,j] = 1
            else:
                N[i,j] = 0
    C = N.copy()
    smalls = np.where(np.sum(N, axis = 1) < c)
    C = np.delete(C, smalls, 0)
    G = np.unique(C, axis = 0) 
    centroids = []
    for i in np.arange(np.size(G,0)):
        O = np.argwhere(G[i,:])
        xs = []
        ys = []
        for j in np.arange(np.size(O,0)):
            x = B[O[j,0],1]
            y = B[O[j,0],2]
            xs.append(x)
            ys.append(y)
        centroid = [np.mean(xs), np.mean(ys)]
        centroids.append(centroid)
    L = np.asarray(centroids)
    return G, L

def step2_ECN(B, G, u): 
    B_prime = B.copy()
    B_prime = np.delete(B_prime, [0,1,2], axis = 1)
    pf_groupings = np.zeros((np.size(G,0), np.size(B_prime,1))) 
    pf_pos_features = []
    pf_neg_features = []
    for i in np.arange(np.size(B_prime,1)):
        mu = np.mean(B_prime[:,i])
        sig = np.std(B_prime[:,i])
        pf_pos_groupings = []
        pf_neg_groupings = []
        for j in np.arange(np.size(G,0)):
            pf_pos_cells = [];
            pf_neg_cells = [];
            indices = np.argwhere(G[j,:])
            for k in indices: 
                if (B_prime[k,i] > (mu + sig*u)):
                    pf_pos_cells.append(1)
                else:
                    pf_pos_cells.append(0)
                if (B_prime[k,i] < (mu - sig*u)):
                    pf_neg_cells.append(1)
                else:
                    pf_neg_cells.append(0)
            pf_pos_cells = np.asarray(pf_pos_cells)
            pf_neg_cells = np.asarray(pf_neg_cells)
            if (np.sum(pf_pos_cells, 0) > 0):
                pf_pos_groupings.append(1)
            else:
                pf_pos_groupings.append(0)
            if (np.sum(pf_neg_cells, 0) > 0):
                pf_neg_groupings.append(1)
            else:
                pf_neg_groupings.append(0)
        pf_pos_groupings = np.asarray(pf_pos_groupings)
        pf_neg_groupings = np.asarray(pf_neg_groupings)
        pf_pos_features.append(pf_pos_groupings)
        pf_neg_features.append(pf_neg_groupings)
    pf_pos_features = np.transpose(np.asarray(pf_pos_features))
    pf_neg_features = np.transpose(np.asarray(pf_neg_features))
    for i in np.arange(np.size(pf_groupings,0)):
        for j in np.arange(np.size(pf_groupings,1)):
            if (pf_pos_features[i,j] == 1 and pf_neg_features[i,j] == 1):
                pf_groupings[i,j] = 1
            else:
                pf_groupings[i,j] = 0
    E = pf_groupings
    return E

def step3_EXY(L, E, G): 
    LEG = np.hstack([L, E, G])
    LE = np.hstack([L, E])
    rows = np.where(np.any(E == 0, axis = 1))
    ls = rows[0].tolist()
    polished = np.delete(LE, ls, 0)
    XY = polished[:,:2]
    return XY