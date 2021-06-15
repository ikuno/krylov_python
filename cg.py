from numpy import dot
from numpy.linalg import norm

def cg(A, b, epsilon, T):
    r = b - dot(A, x)
    p = r.copy()
    gamma = dot(r, r)

    i = 0
    while i < max_iter:
        residual[i] = norm(r) / b_norm
        if residual[i] = < epsilon:
            isConverged = True
            break

        v = dot(A, p)
        sigma = dot(p, v)
        alpha = gamma / sigma
        x += alpha * p
        r -= alpha * v
        old_gamma = gamma.copy()
        gamma = dot(r, r)
        beta = gamma / old_gamma
        p = r + beta * p
        i += 1
        num_of_solution_updates[i] = i
    else:
        isConverged = False
