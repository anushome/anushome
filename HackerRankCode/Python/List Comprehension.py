# Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer n . Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i+j+k is not equal to n. Here, 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z. Please use list comprehensions rather than       multiple loops, as a learning exercise.


# Code 
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
    ans = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)
    if i+j+k != n       ]
    print(ans)
