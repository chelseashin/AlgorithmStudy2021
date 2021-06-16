import sys 
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline 
length, width, height = map(int, input().rstrip().split(" ")) 
n = int(input().rstrip()) 
cubes = [] 
for _ in range(n): 
    a, b = map(int, input().rstrip().split(" ")) 
    cubes.append([2**a, b]) 
    cubes = sorted(cubes, key=lambda x: -x[0]) 
    count = 0 
    PF = True 
def recursive_func(l, w, h): 
    global PF, cubes, count 
    if(PF == False): 
        return 
    if(l == 0 or w == 0 or h == 0): 
        return 
    for i in range(len(cubes)): 
        if(cubes[i][1] > 0 and l >= cubes[i][0] and w >= cubes[i][0] and h >= cubes[i][0]): 
            count += 1 
            cubes[i][1] -= 1 
            recursive_func(l, w, h-cubes[i][0]) 
            recursive_func(cubes[i][0], w-cubes[i][0], cubes[i][0]) 
            recursive_func(l-cubes[i][0], w, cubes[i][0]) 
            return 
        PF = False 
    return recursive_func(length, width, height) 
    
if(PF == False): 
    print(-1) 
else: 
    print(count)

#출처: https://zereight.tistory.com/663 [Zereight's Blog]