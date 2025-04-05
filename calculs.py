from math import tan, pi

def get_series(b: float, theta: float):
    # get exact series (we calculated that it ends up being b/(1+tan(theta))
    return b/(1+tan(theta))

def tan_limit(n: int, theta: float):
    # limt[n->inf] (tan(theta))^n
    t = tan(theta) ** n

    return t

def approximate_limit_series(b: float, n: int, theta: float):
    """
    `b`: side of the square \\
    `n`: approximate limit -> n \\
    `theta`: angle
    """
    c = 0

    # limit[n->inf] of b(-tan)^k 
    for n in range(0,n+1): #n+1 cuz programming >:(
        c += b*(-tan(theta)) ** n 

    t = tan_limit(n=n,theta=theta)

    return(c + t)

if __name__ == '__main__':
    n = 1000000
    theta = pi/6
    b = 6

    print(f"tan lim: {tan_limit(n, theta)}")
    print(f"Limit: {approximate_limit_series(b=b, n=n, theta=theta)}")
    print(f"b/(1 + tan): {get_series(b=b, theta=theta)}")

