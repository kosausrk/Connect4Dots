import os 
import time 

rows, columns = 7,6
grid  = [[0 for x in range(rows)] for y in range(columns)]

winner = 0 #global variable to measure who won, 1 means player 1 won, 2 means player 2 won  

def displayGrid():
  print(f"     1  2  3  4  5  6  7 ")
  print(f"\n  -------------------------")
  numThing = 1
  for x in grid:
    print(str(numThing) + " | "  + str(x) + " |" + "\n \n")
    numThing += 1 
  print(f"  - - - - - - - - - - - - - \n")
  print(f"  - - - - - - - - - - - - - ")


def playToken(col, player):
  for sublist in reversed(grid):
    if sublist[col-1] == 0: #checks if open space
      if player == 1:
        sublist[col-1] = 1
        break
      if player == 2:
        sublist[col-1] = 2
        break

def forcedToken(row, col,player):
  if player == 1:
    grid[row-1][col-1] = 1
  if player == 2:
    grid[row-1][col-1] = 2


def checkVerticalWinnerByColumn(col):
  count1 = 0
  count2 = 0
  for x in grid:
    if x[col-1] == 1:
      count1 += 1
      count2 = 0 
    if x[col-1] == 2:
      count2 += 1
      count1 = 0
    if count1 == 4:
      return 1
    if count2 == 4:
      return 2
  return 0
  
def checkVerticalWinner():
  for x in range(7):
    w = checkVerticalWinnerByColumn(x)
    if w == 1 or w == 2:
      return w 
  return 0 
    
  

def checkHorizontalWinnerByRow(row):
  rowCount1 = 0
  rowCount2 = 0
  for item in grid[row-1]:    
    if item == 1:
      rowCount1 += 1
      rowCount2 = 0
    if item == 2:
      rowCount2 += 1
      rowCount1 = 0
    if rowCount1 == 4:
      return 1 
    if rowCount2 == 4:
      return 2

def checkHorizontalWinner():
  for x in range(6):
    w = checkHorizontalWinnerByRow(x)
    if w == 1 or w == 2:
      return w 
  return 0


def checkDiagonalWinnerByPoint(row,col):
  #checking what directions a point can have 
  upright = False
  upleft = False
  downright = False
  downleft = False
  if row - 3 >= 0 and col - 3 >= 0:
    upleft = True 
  if row - 3 >= 0 and col + 3 <= 6: 
    upright = True
  if row + 3 <= 6 and col - 3 >= 0:
    downleft = True 
  if row + 3 <= 6 and col + 3 <= 6:
    downright = True 

  #iterating through diagonals 
  if upright == True:
    uprightCount1 = 0
    uprightCount2 = 0
    for x in range(4):
      if grid[row-x][col+x] == 1:
        uprightCount1 += 1
      if grid[row-x][col+x] == 2:
        uprightCount2 += 1 
      if uprightCount1 == 4:
        return 1
      if uprightCount2 == 4:
        return 2
    return 0 
  if upleft == True:
    upleftCount1 = 0
    upleftCount2 = 0
    for x in range(4):
      if grid[row-x][col-x] == 1:
        upleftCount1 += 1
      if grid[row-x][col-x] == 2:
        upleftCount2 += 1
      if upleftCount1 == 4:
        return 1 
      if upleftCount2 == 4:
        return 2 
    

  if downleft == True: #This is the only exception that goes out of range (out of bound), because if you test every direction you see that in the middle peice (3,4)  you can go downleft but going through the loop you see in the 4th iteration (down then left each time) it would go outside the grid. This doesn't happen to other directions because there is enough space. 
    downleftCount1 = 1
    downleftCount2 = 1
    for x in range(3):
      if grid[row+x][col-x] == 1:
        downleftCount1 += 1
      if grid[row+x][col-x] == 2:
        downleftCount2 += 1
      if downleftCount1 == 4:
        return 1 
      if downleftCount2 == 4:
        return 2 
    return 0 
  
  if downright == True: #WORKING
    downrightCount1 = 0
    downrightCount2 = 0
    for x in range(4):
      if grid[row+x][col+x] == 1:
        downrightCount1 += 1
      if grid[row+x][col+x] == 2:
        downrightCount2 += 1
      if downrightCount1 == 4:
        return 1 #function returns 1 if player 1 wins
      if downrightCount2 == 4:
        return 2
  return 0 #returns 0 if nothing happens 
      
#use map() to use func across all elements or numpy vectorize 

def checkDiagonalWinner():
  #hours wasted here: 1
  rowCount = 0 
  colCount = 0
  for x in grid:
    rowCount += 1
    for y in x:
      if colCount == 7: #reset once hit final column 
        colCount = 0 
      colCount += 1
      w = checkDiagonalWinnerByPoint(rowCount-1, colCount-1)
      if w == 1 or w == 2:
        return w
  return 0 

def checkWinner():
  w = checkVerticalWinner()
  y = checkHorizontalWinner()
  z = checkDiagonalWinner()
  if 1 in [w,y,z]:
    return 1 
  if 2 in [w,y,z]:
    return 2 
  return 0 


while checkWinner() == 0:
  ask1 = int(input("Player 1 Pick a column"))
  playToken(ask1, 1)
  os.system('clear')
  displayGrid()
  ask2 = int(input("Player 2 pick a column"))
  playToken(ask2, 2)
  os.system('clear')
  displayGrid()

  if checkWinner() != 0:
    win = checkWinner()
    if win == 1:
      print("PLayer 1 won")
    if win == 2:
      print("Player 2 won")


#Play tokens accept regular  column positions. Ex: playToken(1,1) will insert in the first row. The index 0 will be calculated inside that function  
