import numpy as np

#1

n = np.arange(10)
print(n)
n1 = n[::-1]
print(n1)
n2 = np.arange(7, 20)[::-1]
print(n2)
n3 = np.arange(1, 10, 2)[::-1]
print(n3)


players_height = np.array([
    1.72, 1.65, 1.88, 1.91,
    1.82, 1.76, 1.80
])

tall_players_ids = np.where(
    players_height > 1.8)[0]
print(tall_players_ids)

print(players_height.ndim)
print(players_height.min())
print(players_height.max())


A = np.array([[3, 4, 5], [1, 2, 3], [4, 5, 6]])
B = np.array([[-2, 5, 1], [7, 0, 2], [-1, 0, 5]])

print(A[0])
print(B[:,2])

print(A[:, 2:3])
print(A[:, [1,2]])

print(A.sum())
print(A.sum(axis=1))
print(A.sum(axis=0))

print(np.mean(A))
print(np.var(A))
print(np.std(A))

print(np.matmul(A, B))
print(np.dot(A, B))
print(np.multiply(A, B))
print(A*B)

print (" --- ")
#2

C = np.array([1,23,4,31,1,1])

values, counts = np.unique(C, return_counts=True)
print(values)
print(counts)

print(set(int(x) for x in C))


x_counts = dict()
for x in C:
    if x not in x_counts:
        x_counts[int(x)] = 1
    else:
        x_counts[int(x)] += 1

print(x_counts)


D = np.arange(1, 10)
E = np.reshape(D, (3,3))
print(E)

F = np.arange(35, 45).reshape((2,5))
print(F)

#3


print(np.random.randint(10, 31, size=6))
print(np.random.randint(102, 160, size=(8)))


#4



A = np.array([[1, 2, 3, 4], [5, 6, -7, 1]])
print(A.ndim)

#5

A = np.array([[1, 2, 3, 4], [5, 6, -7, 1]])

print(A.ndim)
print(A.size)

#6

G = np.array([[23, 45, 112, 150, 43, 254, 95, 8]])
G1 = G[G > 100]
print(G1)

H = np.array([[10, 21, 32, 43, 54, 65, 76, 87]])

H1 = H[H % 2 == 1 ]
print(H1)

#7

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

print(A[1,2])

#8

A = np.arange(1, 100)
A1 = A[A % 11 == 0]
print(A1)

#9

A = np.arange(6, 36)
A = np.reshape(A, (5,6))
print(A)
A = np.reshape(A, (2,15))
print(A)

#10

A = np.arange(51, 60)
A = np.reshape(A, (3,3))
print(A)

print(" --- ")

#1.11 to 1.20
#1

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

print(np.linalg.det(A))
print(A.min())
print(A.max())
print(A.trace())

#2

A = np.random.normal(loc=0, scale=1, size=(3,3))
B = np.random.normal(loc=5, scale=1, size=(3,3))

print(A*10)
print(A[1][1])
print(A.transpose())
print(A.trace())
print(A.sum())

print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(np.matmul(A, B))


#4

A = np.array([23, 45, 124, 112, 150, 43, 25, 17, 268, 254, 95, 97, 8])

# listo =[int(x) for x in A.flatten() if x > np.mean(A)]

listo = A[A > np.mean(A)]

print(listo)
print(listo.size)







