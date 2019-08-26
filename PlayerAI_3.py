# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 08:50:13 2019

@author: MohamedElfatih
"""
from BaseAI_3 import BaseAI
import time

#time for deciding which move
timeLimit = 0.1
allowance = 0.0
class PlayerAI(BaseAI):
    def __init__(self):
        self.w0 = 1
        self.w1= .1
        self.w2= .02

    #@param:grid  >> the board state
    #returns: best move 
    def getMove(self,grid):
        moves = grid.getAvailableMoves()
        move_value = dict()
        for move in moves:
            move_value[move] = 0 
        #initially the time will be 0
        passedTime = 0
        depth = 1
        #the move that will be returned after the depth first search
        bestMove = None
        bestValue = -9999
        while passedTime < (timeLimit + allowance) - passedTime:
            
            maxMove = None
            maxVal  = -9999
            
            #sorting moves according to 
            #move_value
            sorted(moves ,  key = lambda x: move_value[x] , reverse = True)
            for move in moves:
                #take time here for beginning
                timeBefore = time.clock()
                gridCopy = grid.clone()
                gridCopy.move(move)
                v = self.Min_move( gridCopy ,-9999 , 9999 , depth)
                move_value[move] = v;
                if(v > maxVal):
                    maxVal =v
                    maxMove = move
                timeAfter = time.clock()
                #time for ending 
                passedTime = passedTime + timeAfter - timeBefore
                
                if(passedTime > timeLimit + allowance):
                    print(passedTime)
                    if(maxVal > bestValue):
                        return maxMove
                    return bestMove
                
                
            #check the move for this depth is better than
            #the previous bestMove
            if (maxVal > bestValue):
                bestValue  = maxVal
                bestMove   = maxMove 
            depth  += 1
            
        print(passedTime)
        print(depth - 1)
        return bestMove
                
    
    
    #@param: grid  >> board state
    #@param:alpha  >> specifying the lower bound for min
    #@param:beta   >> specifying the max bound for max
    #@param:depth  >> used for cuttoff test
    #returns:      >> minmax of the move when it is player max
    def Max_move(self, grid , alpha , beta , depth):
        if (depth  == 0) or (not grid.canMove()):
            return self.eval_h(grid)
        
        maxValue  = -999
        availableMoves = grid.getAvailableMoves()
        
        for move in availableMoves:
            gridCopy = grid.clone()
            gridCopy.move(move)
            v  = self.Min_move( gridCopy, alpha , beta , depth - 1)
            if v > maxValue :
                maxValue = v
                
            if maxValue > beta:
                return maxValue
            
            if(maxValue > alpha):
                alpha  = maxValue
                
            
        return maxValue;
  
    #@param: grid  >> board state
    #@param:alpha  >> specifying the lower bound for min
    #@param:beta   >> specifying the max bound for max
    #@param:depth  >> used for cuttoff test
    #returns:      >> minmax of the move when it is player min
    def Min_move(self,grid , alpha , beta , depth):
            if (depth  == 0) or (not grid.canMove()):
                return self.eval_h(grid)
            
            minValue  = 999
            availableCells = grid.getAvailableCells()
            tiles = [2,4]
            
            for move in availableCells:
                for i in range(0,1):
                    gridCopy = grid.clone()
                    gridCopy.setCellValue(move , tiles[i])
                    v  = self.Max_move(gridCopy , alpha , beta , depth - 1)
                    if v < minValue :
                        minValue = v
                        
                    if minValue < alpha:
                        return minValue
                    
                    if(minValue < beta):
                        beta  = minValue
                    
            return minValue;
        
    #@param: grid >> board state
    #returns: the expected minimax value of this state for player max
    def eval_h(self,grid):
        map1 = list()
        map1 = grid.map
        sum1 = 0
        for i in map1:
            for j in i:
                sum1 +=j
        #heuristic for avg value in the board
        avgTile = sum1/16
        
        #heuristics for corners
        cells = [[30,15,5,3],[15,5,3,1],[5,3,1,0],[3,1,0,0]]
        sum2 = 0
        for i in range(0,len(map1)):
            for j in range(0,len(map1[i])):
                sum2 += map1[i][j] * cells[i][j]
                
        
        pen = 0
        for i in range(0,len(map1)):
            for j in range(0,len(map1[i])):
                if(j != len(map1[i]) - 1):
                    pen += abs(map1[i][j]  - map1[i][j+1])
                if(i != len(map1) -1):
                    pen += abs(map1[i][j]  - map1[i+1][j])

            
        corners= sum2
            
        return self.w0*len(grid.getAvailableCells())+ self.w1* avgTile + self.w2*sum2;
                          
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    