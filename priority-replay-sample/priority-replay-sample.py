import numpy as np

def priority_replay_sample(priorities, alpha, beta):
    priorities = np.asarray(priorities, dtype = float)
    N = priorities.size
    
    # 1. Compute powered priorities
    powered = priorities ** alpha
    
    # 2. Compute sampling probabilities
    probs = powered / np.sum(powered)
    
    # 3. Compute raw importance sampling weights
    weights = (N * probs) ** (- beta)
    
    # 4. Normalize weights by maximum weight
    weights = weights / np.max(weights)
    
    return [probs.tolist(), weights.tolist()]