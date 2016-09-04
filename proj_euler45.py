n = 1
triangles = []
pentagons = []
hexagons = []
while n < 100000: #assuming it lies below n = 1000000
    triangles.append(n*(n+1)/2)
    pentagons.append(n*(3*n-1)/2)
    hexagons.append(n*(2*n-1))
    n += 1

print set(triangles) & set(pentagons) & set(hexagons)