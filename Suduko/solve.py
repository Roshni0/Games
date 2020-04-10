def presentMiniGrid(suduko,row,col,num): #mini grid check to see if no. there
  for i in range(3): 
    for j in range(3): 
      if(suduko[i+row][j+col] == num): 
        return True
  return False
def presentRow(suduko,row,num): #row check to see if no. there
  for i in range(9): 
    if(suduko[row][i] == num): 
      return True
  return False
def presentCol(suduko,col,num): #column check to see if no. there
  for i in range(9): 
    if(suduko[i][col] == num): 
      return True
  return False
def check(suduko,row,col,num): #check to make sure it is okay to put there, given column, row and mini grid
    return not presentRow(suduko,row,num) and not presentCol(suduko,col,num) and not presentMiniGrid(suduko,row - row%3,col - col%3,num) 
def emptyLoc(suduko,store): #find a thing that has nothing
  for row in range(9): 
    for col in range(9): 
      if(suduko[row][col]==0): 
        store[0]=row 
        store[1]=col 
        return True
  return False
def solve(suduko): 
  store=[0,0]     
  if(not emptyLoc(suduko,store)): 
      return True
  row=store[0] 
  col=store[1] 
  for num in range(1,10): 
    if(check(suduko,row,col,num)): 
      suduko[row][col]=num 
      if(solve(suduko)): 
        return True
      suduko[row][col] = 0      
  return False 
suduko = []
for x in range(9):
  #differentiate each value by a space
  #if no value, enter 0
  x = list(map(int, input("Enter row: ").split()))
  suduko.append(x)
if(solve(suduko)): 
  for i in range(9): 
    for j in range(9): 
      print suduko[i][j], 
    print ('')     
else: 
  print ("Cannot be solved at this given time :/")
