import numpy as np

def gwo(bench_func, dim, agents, max_iter, low_b, up_b):
    # initial positions
    a_position = np.zeros(dim)
    a_score = np.inf

    b_position = np.zeros(dim)
    b_score = np.inf

    d_position = np.zeros(dim)
    d_score = np.inf

    positions = np.random.uniform(low_b, up_b, (agents, dim))
    conv_curve = []
    log_output = ""

    # start iteration
    for t in range(max_iter):
        for i in range(agents):
            
            # clip position outside boundary
            positions[i] = np.clip(positions[i], low_b, up_b)
            fitness = bench_func(positions[i])

            # update best score
            if fitness < a_score:
                a_score = fitness
                a_position = positions[i].copy()
            elif fitness < b_score:
                b_score = fitness
                b_position = positions[i].copy()
            elif fitness < d_score:
                d_score = fitness
                d_position = positions[i].copy()
        
        # decreasing search zone
        a = 2 - t * (2 / max_iter)
        for i in range(agents):
            for j in range(dim):

                # update wolves position
                r1 = np.random.rand()
                r2 = np.random.rand()
                A1 = 2 * a * r1 - a
                C1 = 2 * r2
                D_alpha = abs(C1 * a_position[j] - positions[i][j])
                X1 = a_position[j] - A1 * D_alpha

                r1 = np.random.rand()
                r2 = np.random.rand()
                A2 = 2 * a * r1 - a
                C2 = 2 * r2
                D_beta = abs(C2 * b_position[j] - positions[i][j])
                X2 = b_position[j] - A2 * D_beta

                r1 = np.random.rand()
                r2 = np.random.rand()
                A3 = 2 * a * r1 - a
                C3 = 2 * r2
                D_delta = abs(C3 * d_position[j] - positions[i][j])
                X3 = d_position[j] - A3 * D_delta

                positions[i][j] = (X1 + X2 + X3) / 3
    
        # save best score
        conv_curve.append(a_score)
        log_output += f"Iteration {t+1}, Best Cost: {a_score:.4f}\n"
    
    return conv_curve, log_output

# rotated hyper-ellipsoid function
def f3(x):
    return sum((sum(x[:i+1]))**2 for i in range(len(x)))

# schwefel function
def f8(x):
    return sum(-xi * np.sin(np.sqrt(abs(xi))) for xi in x)