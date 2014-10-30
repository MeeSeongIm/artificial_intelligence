
# A* algorithm: autonomous code.  
# 0 is an allowable path and 1 is a wall. Computer starts at the lower left corner and searches for 2. 

grid = [[0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 2]]

 
def trea_hunt(x, y):
    if grid[x][y] == 2:
        print("found at (%d,%d)" % (x+1, y+1))
        return True
    elif grid[x][y] == 1:
        print("wall at (%d,%d)" % (x+1, y+1))
        return False
    elif grid[x][y] == 3:
        print("visited at (%d,%d)" % (x+1, y+1))
        return False
         
    print("visiting (%d,%d)" % (x+1, y+1))
    grid[x][y] = 3   
 
    if ((x < len(grid)-1 and trea_hunt(x+1, y))
        or (y > 0 and trea_hunt(x, y-1))
        or (x > 0 and trea_hunt(x-1, y))
        or (y < len(grid)-1 and trea_hunt(x, y+1))):
        return True
    
    return False
 
trea_hunt(10, 0) 
 
 
 
 
 
