#reshape the matrix
def reshape(mat,r,c):
    m,n = len(mat),len(mat[0])
    flat = []
    matrix = []

    if r*c!=m*n:
        return mat

    for i in mat:
        flat = flat + i

    for i in range(0,len(flat),c):
        matrix.append(flat[i:i+c])

    return matrix            


mat = [[1,2],[3,4],[5,6]]
r =3
c=2

print(reshape(mat,r,c))