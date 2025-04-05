from math import tan, pi
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def graph_series(b, theta):
    """
    Graphical representation of the function calculated in question 1
    """
    x = np.arange(0, 50, 1)
    plt.plot(
        x, b*(1-(-tan(theta)) ** (x+1)) / (1+tan(theta))
    )
    plt.show()

def get_convergence_point_1(b: float, theta: float):
    """
    Get the exact answer (we calculated that it ends up being b/(1+tan(theta))
    """
    return b/(1+tan(theta))

def tan_limit(a:int, j: int, theta: float):
    """
    Calculate the limit[n->j] (tan(theta))^n
    """
    t = a*(-tan(theta)) ** j

    return t

def approximate_limit_series(a:int, b: float, j: int, theta: float):
    """
    Approximates the point for lim approaches j for a given angle theta < pi/4
    `a`: starting point \\
    `b`: side of the square \\
    `j`: approximate limit n -> j \\
    `theta`: angle
    """
    series_sum = 0

    series_sum = b*(1-(-tan(theta)) ** (j+1)) / (1+tan(theta))

    t = tan_limit(a=a, j=j,theta=theta)

    return(series_sum + t)

def reflect_vectors(a: np.ndarray,b: np.ndarray):
    """
    Function to reflect vectors
    """
    r = 2 * (np.dot(a, b)/np.linalg.norm(b)**2) * b - a

    return r

def problem2(n, l):
    k = 10
    # n = number of sides
    # l = length of one side
    fig, ax = plt.subplots()
    square = [
        [
            [0.0,float(n)],
            [0.0,0.0],
        ],
        [
            [float(n),float(n)],
            [float(n),0.0],
        ],
        [
            [0.0,float(n)],
            [float(n),float(n)],
        ],
        [
            [0.0,0.0],
            [float(n),0.0],
        ],
    ]
    for side in square:
        ax.plot(
            side[0], side[1], 
        )

    plt.show()

if __name__ == '__main__':
    a = 2
    j = 1000000
    theta = pi/6
    b = 6
    
    graph_series(b=b, theta=theta)
    problem2(4, 2)

    # fig, ax = plt.subplots()
    # v1 = np.array([[0,1],[0,1]]).tolist()
    # ax.plot(v1[0], v1[1])
    # v2 = np.array([[0,2],[2,0]]).tolist()
    # ax.plot(v2[0], v2[1])
    # v3 = reflect_vectors(v1, v2).tolist()
    # ax.plot(v3[0], v3[1])
    # plt.show()

    print(f"Tangent limit: {tan_limit(a=a, j=j, theta=theta)}")
    for i in range(1,20):
        print(f"Approximation: {approximate_limit_series(a=a, b=b, j=i, theta=theta)}")
    print(f"Exact number: {get_convergence_point_1(b=b, theta=theta)}")