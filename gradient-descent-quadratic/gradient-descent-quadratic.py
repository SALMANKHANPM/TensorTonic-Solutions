def grad(a, b, x):
    return 2 * (a * x) + b

def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    loss = 0 
    
    for s in range(steps):
        g= grad(a, b, x0)
        x0 = x0 - lr * g
        loss = x0

    return loss