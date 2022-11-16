def get_val(arr,i,j,L,H):
    if (i < 0 or i >= L or j < 0 or j >= H):
        return 0
    else :
        return arr[i][j]
    
    
    
def find_max_block(arr,r,c,L,H,size):
    
    global maxsize
    global cntarr 
    print(cntarr)
    if ( r >= L or c>=H):
        return 
    cntarr[r][c] = 1
    
    size += 1
    if size > maxsize:
        maxsize = size
        
    #search for all direction
    
    directions = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
    
    for i in range(0,7):
        newi = r + directions[i][0]
        newj = c + directions[i][1]
        val = get_val(arr,newi,newj,L,H)
        if (val > 0 and (cntarr[newi][newj] == 0)):
            find_max_block(arr,newi,newj,L,H,size)
    cntarr[r][c] = 0
        
def get_max_ones(arr,rmax,cmax):
    global maxsize
    global size
    global cntarr 
    
    for i in range(0,rmax):
        for j in range(0,cmax):
            if arr[i][j] == 1:
                find_max_block(arr,i,j,rmax,cmax,0)
    return maxsize


zarr = [[1,0,0,0,0],[0,1,0,0,1],[0,0,0,0,1],[1,0,0,0,1],[0,1,0,1,0]]

rmax = 5
cmax = 5
maxsize = 0
size = 0

cntarr = rmax * [cmax*[0]]

print("number of max 1's are  ",get_max_ones(zarr,rmax,cmax))