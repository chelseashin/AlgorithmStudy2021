def main(blocks):
    result = []
    pyramid = list()
    for i, block in enumerate(blocks):
        pyramid.append([-200]*len(blocks))
        j, value = tuple(block)
        pyramid[i][j] = value
        for k in range(j, i):
           pyramid[i][k+1] = pyramid[i-1][k] - pyramid[i][k]
        for k in range(j, 0, -1):
           pyramid[i][k-1] = pyramid[i-1][k-1] - pyramid[i][k] 
           continue

    for i in range(len(blocks)):
        for j in range(0, i+1):
            result.append(pyramid[i][j])
    return result

print(main([[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]))
print(main([[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]))